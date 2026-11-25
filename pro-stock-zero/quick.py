"""Quick test of one arm on the 5 cross-session tasks, 2 runs each, against stored baselines.
python3 quick.py <arm> [runs]"""
import json, subprocess, sys
from pathlib import Path
H = Path(__file__).resolve().parent
arm, n = sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 2
T = sys.argv[3].split(",") if len(sys.argv) > 3 else ["s1_tickets", "s2_expenses", "s3_letters", "s4_letters", "s5_faq"]
base = sys.argv[4].split(",") if len(sys.argv) > 4 else ["bare", "state"]
tag = arm + ("_" + T[0][:2] if len(sys.argv) > 3 else "")
plan = H / "runs" / f"plan_q_{tag}.json"
plan.write_text(json.dumps([{"task": t, "arm": arm, "rep": r} for t in T for r in range(n)]))
subprocess.run([sys.executable, str(H / "run.py"), f"q_{tag}", str(plan)], check=True, stdout=subprocess.DEVNULL)
rows = []
for b in ["calib", "calib2", "r1a"] + [d.name for d in (H / "runs").glob("q_*") if d.name != f"q_{tag}"]:
    rows += [json.loads(x) for x in (H / "runs" / b / "results.jsonl").read_text().splitlines()]
rows += [json.loads(x) for x in (H / "runs" / f"q_{tag}" / "results.jsonl").read_text().splitlines()]
def cell(t, a):
    rs = [r for r in rows if r["task"] == t and r["arm"] == a]
    return f"{sum(r['pass'] for r in rs)}/{len(rs)} ${sum(r['cost_usd'] for r in rs)/len(rs):.4f}" if rs else "-"
arms = base + [arm]
print("| task | " + " | ".join(arms) + " |\n" + "|---" * (len(arms) + 1) + "|")
for t in T:
    print(f"| {t} | " + " | ".join(cell(t, a) for a in arms) + " |")
for a in arms:
    rs = [r for r in rows if r["arm"] == a and r["task"] in T]
    if not rs:
        continue
    print(f"{a}: {sum(r['pass'] for r in rs)}/{len(rs)} pass, ${sum(r['cost_usd'] for r in rs)/len(rs):.4f} per task")
