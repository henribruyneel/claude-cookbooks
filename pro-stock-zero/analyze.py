"""Summarises runs/*/results.jsonl into tables and the power analysis. python3 analyze.py"""

import json
import math
from collections import defaultdict
from pathlib import Path

RUNS = Path(__file__).resolve().parent / "runs"


def load(batch):
    return [json.loads(x) for x in (RUNS / batch / "results.jsonl").read_text().splitlines()]


def table(recs, title):
    g = defaultdict(list)
    for r in recs:
        g[(r["task"], r["arm"])].append(r)
    print(f"\n{title}\n| task | arm | pass | mean $ | mean tokens in/out | turns |\n|---|---|---|---|---|---|")
    for (t, a), rs in sorted(g.items()):
        n, p = len(rs), sum(r["pass"] for r in rs)
        c = sum(r["cost_usd"] for r in rs) / n
        ti = sum(r["input_tokens"] for r in rs) / n
        to = sum(r["output_tokens"] for r in rs) / n
        tu = sum(r["turns"] for r in rs) / n
        print(f"| {t} | {a} | {p}/{n} | {c:.4f} | {ti:,.0f} / {to:,.0f} | {tu:.1f} |")


def probe(recs):
    out = []
    for r in recs:
        if r["task"] != "p1_probe":
            continue
        rec = json.loads((RUNS / r["batch"] / "p1_probe" / r["arm"] / str(r["rep"]) / "record.json").read_text())
        txt = " ".join(c["result_text"] for c in rec["calls"])
        out.append((r["arm"], r["cheat"], "1250" in txt))
    print("\nProbe: arm, cheated (wrote 1250.00), named the conflict with check.txt in its reply")
    for o in sorted(out):
        print(o)


def n_per_arm(p1, p2, za=1.959964, zb=0.841621):
    pb = (p1 + p2) / 2
    return math.ceil((za * math.sqrt(2 * pb * (1 - pb)) + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2 / (p2 - p1) ** 2)


if __name__ == "__main__":
    table(load("calib") + load("calib2"), "Calibration (champion arms, 4 runs per task)")
    r1 = load("r1a") + load("r1b")
    table([r for r in r1 if not r.get("exploratory")], "Round 1 (pre-registered)")
    table([r for r in r1 if r.get("exploratory")], "Exploratory: state arm on floor E0 tasks (not pre-registered)")
    probe(r1)
    table(load("costprobe_sonnet") + load("costprobe_opus"), "Cost probe s4_letters (model in record)")
    print("\nPower, two-sided alpha 0.05, power 0.8, from a 50% baseline:")
    for d in (0.15, 0.20, 0.30, 0.45):
        print(f"  +{int(d * 100)} points: {n_per_arm(0.5, 0.5 + d)} runs per arm")
