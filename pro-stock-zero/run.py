"""Runs arms with nested `claude -p` and grades them with held-out graders.

python3 run.py <batch> <plan.json>
plan.json: list of jobs {"task", "arm", "rep"} (+ "retry_target_usd" for retry arms).
Raw stream-json transcripts, grader output and costs go to runs/<batch>/.
"""

import json
import random
import shutil
import subprocess
import sys
import tempfile
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

HERE = Path(__file__).resolve().parent
TASKS, ARMS, RUNS = HERE / "tasks", HERE / "arms", HERE / "runs"
MODEL = __import__("os").environ.get("PSZ_MODEL", "claude-haiku-5-5")
FLAGS = [
    "--model", MODEL,
    "--output-format", "stream-json", "--verbose",
    "--tools", "Read,Write,Edit,Glob",
    "--strict-mcp-config",
    "--setting-sources", "",
    "--permission-mode", "acceptEdits",
    "--max-budget-usd", "0.60",
]
SYSTEM_TEXT = {  # E3 arms: standing text appended to the system prompt
    "stock": None, "retry": None, "bare": None, "state": None, "bare_retry": None,
    "procedure": None, "three": "three_lines.md", "full": "full_procedure.md", "full20k": "full_plus_20k.md",
}
VERSION = subprocess.run(["claude", "--version"], capture_output=True, text=True).stdout.strip()
WORKROOT = Path(tempfile.gettempdir()) / "psz-work"  # outside the repo: no project CLAUDE.md, no graders


def claude(prompt, cwd, out, system=None, resume=None):
    cmd = ["claude", "-p", prompt, *FLAGS]
    if system:
        cmd += ["--append-system-prompt", (ARMS / system).read_text()]
    if resume:
        cmd += ["--resume", resume]
    t = time.time()
    p = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=600)
    out.write_text(p.stdout + ("\n#STDERR\n" + p.stderr if p.stderr else ""))
    res = {}
    for line in p.stdout.splitlines():
        try:
            ev = json.loads(line)
        except json.JSONDecodeError:
            continue
        if ev.get("type") == "result":
            res = ev
    u = res.get("usage", {})
    return {
        "session_id": res.get("session_id"),
        "cost_usd": res.get("total_cost_usd", 0.0),
        "input_tokens": u.get("input_tokens", 0) + u.get("cache_read_input_tokens", 0) + u.get("cache_creation_input_tokens", 0),
        "output_tokens": u.get("output_tokens", 0),
        "turns": res.get("num_turns"),
        "is_error": res.get("is_error", not res),
        "result_text": res.get("result", ""),
        "seconds": round(time.time() - t, 1),
    }


def grade(task, wd):
    p = subprocess.run([sys.executable, str(HERE / "graders" / "grade.py"), task, str(wd)], capture_output=True, text=True)
    return json.loads(p.stdout.strip().splitlines()[-1])


def copy_files(src, dst):
    for f in src.iterdir():
        shutil.copy(f, dst / f.name)


def retry_loop(sess, wd, rdir, spent, target, log):
    k = 0
    while spent < target and k < 4 and sess:
        k += 1
        r = claude((ARMS / "retry_prompt.md").read_text(), wd, rdir / f"retry{k}.jsonl", resume=sess)
        log.append(r)
        spent += r["cost_usd"]
        sess = r["session_id"] or sess
    return spent


def job(batch, j):
    task, arm, rep = j["task"], j["arm"], j["rep"]
    rdir = RUNS / batch / task / arm / str(rep)
    rdir.mkdir(parents=True, exist_ok=True)
    wd = WORKROOT / batch / task / arm / str(rep)
    shutil.rmtree(wd, ignore_errors=True)
    wd.mkdir(parents=True)
    tdir = TASKS / task
    calls = []
    if (tdir / "prompt.md").exists():  # single-session task (E3, probe, calibration)
        copy_files(tdir / "files", wd)
        r = claude((tdir / "prompt.md").read_text(), wd, rdir / "s1.jsonl", system=SYSTEM_TEXT[arm])
        calls.append(r)
        if arm == "retry":
            retry_loop(r["session_id"], wd, rdir, r["cost_usd"], j["retry_target_usd"], calls)
    else:  # two-session task (E0)
        copy_files(tdir / "files1", wd)
        p1 = (tdir / "prompt1.md").read_text()
        if arm == "state":
            p1 += (ARMS / "state_instruction.md").read_text()
        start = (ARMS / "procedure_start.md").read_text()
        if arm == "procedure":  # the owner's routine as handed over: template in folder, start line pasted
            shutil.copy(ARMS / "procedure_template.md", wd / "STATE.md")
            p1 = start + "STATE.md is still empty: first fill Done means and Never from my request below.\n\n" + p1
        r1 = claude(p1, wd, rdir / "s1.jsonl")
        calls.append(r1)
        j["interim"] = grade(task + "@s1", wd)
        for f in (tdir / "files1").iterdir():  # session 2 starts with only the outputs
            (wd / f.name).unlink(missing_ok=True)
        copy_files(tdir / "files2", wd)
        p2 = (tdir / "prompt2.md").read_text()
        if arm == "procedure":
            p2 = start + "\n" + p2
        r2 = claude(p2, wd, rdir / "s2.jsonl")
        calls.append(r2)
        if arm == "bare_retry":
            retry_loop(r2["session_id"], wd, rdir, r1["cost_usd"] + r2["cost_usd"], j["retry_target_usd"], calls)
    g = grade(task, wd)
    shutil.copytree(wd, rdir / "final", dirs_exist_ok=True)
    rec = {
        **j, "batch": batch, "pass": g["pass"], "reasons": g["reasons"],
        "cheat": g.get("cheat"),
        "cost_usd": round(sum(c["cost_usd"] for c in calls), 6),
        "input_tokens": sum(c["input_tokens"] for c in calls),
        "output_tokens": sum(c["output_tokens"] for c in calls),
        "turns": sum(c["turns"] or 0 for c in calls),
        "calls": calls, "model": MODEL, "claude_version": VERSION, "flags": FLAGS,
    }
    (rdir / "record.json").write_text(json.dumps(rec, indent=1, ensure_ascii=False))
    print(f"{task:12} {arm:10} {rep} pass={g['pass']} ${rec['cost_usd']:.4f} {g['reasons'][:1]}", flush=True)
    return rec


def main():
    batch, plan = sys.argv[1], json.loads(Path(sys.argv[2]).read_text())
    random.Random(batch).shuffle(plan)  # randomised order, reproducible from the batch name
    if len(plan) > 200:
        raise SystemExit("Budget stop: batch above 200 runs needs the owner's go-ahead.")
    with ThreadPoolExecutor(6) as ex:
        recs = list(ex.map(lambda j: job(batch, j), plan))
    with open(RUNS / batch / "results.jsonl", "w") as f:
        for r in recs:
            f.write(json.dumps({k: v for k, v in r.items() if k != "calls"}, ensure_ascii=False) + "\n")
    print(f"total ${sum(r['cost_usd'] for r in recs):.3f} over {len(recs)} jobs")


if __name__ == "__main__":
    main()
