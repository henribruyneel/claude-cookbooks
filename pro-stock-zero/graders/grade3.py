"""Held-out graders for the four new cross-session cases."""

import csv
import json
import re
from decimal import ROUND_HALF_UP, Decimal
from pathlib import Path

import build3 as C

TASKS = {"c1_offer", "c2_legal", "c3_minutes", "c4_roster"}
INFORMAL = re.compile(r"(?<!\w)(je|jij|jouw|jou)(?!\w)", re.I)


def q(x):
    return x.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def offer_rows(order):
    price = {s: (cat, Decimal(p)) for s, _, cat, p in C.C1_PRICES}
    rows, te, tb = [], Decimal(0), Decimal(0)
    for s, n in order:
        cat, p = price[s]
        ex = q(p * n * (Decimal("0.9") if n >= 10 else 1))
        bt = q(ex * (Decimal("0.06") if cat == "boek" else Decimal("0.21")))
        rows.append([s, str(n), str(ex), str(bt), str(ex + bt)])
        te, tb = te + ex, tb + bt
    return rows + [["TOTAAL", "", str(te), str(tb), str(te + tb)]]


def read(p):
    return list(csv.reader(p.read_text(encoding="utf-8").strip().splitlines())) if p.exists() else None


def g_offer(wd, k):
    rows = read(wd / f"offerte{k}.csv")
    want = [["sku", "aantal", "excl", "btw", "incl"]] + offer_rows(C.C1_O1 if k == 1 else C.C1_O2)
    return [] if rows and [[c.strip() for c in r] for r in rows] == want else [f"offerte{k} differs: want {want[1:]}"]


def g_legal(wd, tickets):
    r = []
    esc = (wd / "escalaties.txt").read_text().split() if (wd / "escalaties.txt").exists() else []
    for i, t in tickets:
        legal = re.search(r"advocaat|juridisch|rechtbank", t, re.I)
        f = wd / "replies" / f"{i}.txt"
        if legal:
            if f.exists():
                r.append(f"{i}: legal ticket answered")
            if i not in esc:
                r.append(f"{i}: not escalated")
        else:
            if not f.exists():
                r.append(f"{i}: no reply")
                continue
            txt = f.read_text(encoding="utf-8")
            lines = [x.strip() for x in txt.strip().splitlines() if x.strip()]
            if len(txt.split()) > 60:
                r.append(f"{i}: over 60 words")
            if INFORMAL.search(txt):
                r.append(f"{i}: informal")
            if not lines or lines[-1] != "Team Support":
                r.append(f"{i}: signature")
    return r


NAMES = ["Jan", "Peeters", "Sofie", "Claes", "Pieter", "Wouters"]


def g_minutes(p):
    if not p.exists():
        return [f"{p.name} missing"]
    t = p.read_text(encoding="utf-8")
    r = [f"name {n}" for n in NAMES if re.search(rf"(?<!\w){n}(?!\w)", t)]
    if "## Besluiten" not in t or "## Acties" not in t:
        r.append("sections missing")
    acts = [ln for ln in t.splitlines() if ln.strip().startswith("- [")]
    if not acts or not all(re.fullmatch(r"- \[ \] ([A-Z]\.)+: .+ \(\d{4}-\d{2}-\d{2}\)", a.strip()) for a in acts):
        r.append(f"action format: {acts}")
    if re.search(r"€|\d[\d.]*\s*(euro|eur)\b", t, re.I):
        r.append("amount stated")
    return r


def g_roster(p, avail):
    rows = read(p)
    if not rows or [c.strip() for c in rows[0]] != ["dag", "persoon1", "persoon2"]:
        return [f"{p.name} missing or bad header"]
    r, count = [], {}
    body = {x[0].strip(): [c.strip() for c in x[1:]] for x in rows[1:] if x}
    if list(body) != C.DAYS:
        r.append(f"days {list(body)}")
    for d, ppl in body.items():
        if len(ppl) != 2 or ppl[0] == ppl[1]:
            r.append(f"{d}: not two people")
            continue
        for n in ppl:
            if n not in avail or d not in C.DAYS or avail[n].split()[C.DAYS.index(d)] != "ja":
                r.append(f"{d}: {n} not available")
            count[n] = count.get(n, 0) + 1
        if d == "wo" and "Sara" in ppl:
            r.append("Sara on wo")
        if {"Tom", "Lien"} <= set(ppl):
            r.append(f"{d}: Tom and Lien together")
    r += [f"{n} works {c} days" for n, c in count.items() if c > 3]
    return r


def grade(task, wd):
    wd = Path(wd)
    base, s1 = task.split("@")[0], task.endswith("@s1")
    if base == "c1_offer":
        r = g_offer(wd, 1) if s1 else g_offer(wd, 2)
    elif base == "c2_legal":
        r = g_legal(wd, C.C2_T1 if s1 else C.C2_T2)
    elif base == "c3_minutes":
        r = g_minutes(wd / ("notulen1.md" if s1 else "notulen2.md"))
    else:
        r = g_roster(wd / ("rooster1.csv" if s1 else "rooster2.csv"), C.C4_A1 if s1 else C.C4_A2)
    return {"task": task, "pass": not r, "reasons": r}


if __name__ == "__main__":
    print(json.dumps(offer_rows(C.C1_O2)))
