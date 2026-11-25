"""Calibration round 2 tasks (added after calibration 1 put 4 of 5 single tasks at ceiling
and all E0 tasks at floor). Same rules as build.py tasks, larger inputs; two new E0 tasks.
"""

import json
import random
import re

import build as B

R = random.Random(2611252)
WRITE = True


def w(*a):
    if WRITE:
        B.write(*a)

# ---------- T1h: 45 tickets, same rules and prompt as T1 ----------
SUBJ = [
    ("Platform down", "Everything is down since this morning."),
    ("Download fails", "The download of the export never finishes."),
    ("Breakdown per region", "Can the breakdown report show regions?"),
    ("Kan niet inloggen", "Sinds gisteren kan ik niet inloggen."),
    ("Login issue", "Some users cannot log in from the office."),
    ("Factuur november", "Graag een kopie van de factuur van november."),
    ("Invoice address", "Please change the address on our invoice."),
    ("Refunded?", "Has my refund been processed?"),
    ("Refund policy", "What is your refund policy for annual plans?"),
    ("Outage?", "Is there an outage? Nothing loads."),
    ("Planned downtime", "When is the next downtime window?"),
    ("Thanks", "Great support, thank you."),
    ("Seats", "We need five more seats."),
    ("Kan niet uitloggen", "Ik kan niet uitloggen op mijn gsm."),
    ("Slow", "Pages are slow but they load."),
]
DOMAINS = ["brouwer.be", "delta.eu", "noord.be", "acme-intern.be", "studio9.be", "lumen.eu"]
PLANS = ["basic", "pro", "enterprise"]


def build_t1h():
    rows = []
    for k in range(45):
        su, b = SUBJ[R.randrange(len(SUBJ))]
        rows.append((
            f"T-{200 + k}", f"user{k}@{R.choice(DOMAINS)}", R.choice(PLANS),
            "closed" if R.random() < 0.15 else "open", su, b,
        ))
    w("t1h_tickets", "files/tickets.jsonl", "".join(
        json.dumps(dict(id=i, email=e, plan=p, status=s, subject=su, body=bd), ensure_ascii=False) + "\n"
        for i, e, p, s, su, bd in rows))
    w("t1h_tickets", "prompt.md", B.T1_PROMPT)
    return rows


# ---------- T2h: 36 expense rows, same rules and prompt as T2 ----------
def build_t2h():
    rows, k = [], 0
    for m in ("2026-09", "2026-10", "2026-11"):
        for _ in range(10):
            k += 1
            cur = "USD" if R.random() < 0.3 else "EUR"
            cents = R.randrange(500, 25000) * (-1 if R.random() < 0.08 else 1)
            a = f"{cents / 100:.2f}"
            if cur == "EUR" and R.random() < 0.6:
                a = a.replace(".", ",")
            rows.append((f"X{k:02d}", f"{m}-{R.randrange(1, 28):02d}",
                         R.choice(["reizen", "software", "maaltijden", "privé"]), a, cur))
    for _ in range(6):  # duplicates
        rows.insert(R.randrange(len(rows)), rows[R.randrange(len(rows))])
    w("t2h_expenses", "files/expenses.csv", "id,date,category,amount,currency\n" + "".join(
        f'{i},{d},{c},"{a}",{cur}\n' for i, d, c, a, cur in rows))
    w("t2h_expenses", "prompt.md", B.T2_PROMPT)
    return rows


# ---------- T5h: 24 invoices, 30 payments, same rules and prompt as T5 ----------
def build_t5h():
    inv = [(f"INV-{n:04d}", R.choice(["Brouwer", "Delta", "Noord", "Lumen", "Ortho", "Vlaskop"]), f"{R.randrange(2000, 90000) / 100:.2f}") for n in range(1, 25)]
    pays = []
    forms = ["INV-{:04d}", "inv {}", "Factuur {:04d}", "INV{:04d}", "factuur {}", "Inv-{}"]
    for n, (code, _, a) in enumerate(inv, 1):
        a = float(a)
        roll = R.random()
        f = R.choice(forms).format(n)
        if roll < 0.35:
            pays.append(("2026-11-01", f, f"{a:.2f}"))
        elif roll < 0.6:
            part = round(a * R.choice([0.3, 0.5, 0.7]), 2)
            pays.append(("2026-11-02", f, f"{part:.2f}"))
            if R.random() < 0.5:
                pays.append(("2026-11-09", R.choice(forms).format(n), f"{a - part:.2f}"))
        elif roll < 0.7:
            pays.append(("2026-11-03", f, f"{a + 5:.2f}"))
        elif roll < 0.8:
            pays.append(("2026-11-04", "overschrijving zonder referentie", f"{a:.2f}"))
    pays = [x for x in pays if not re.search(r"(?:inv|factuur)[\s-]*0*(4|11)$", x[1], re.I)]
    pays.append(("2026-11-05", "INV-0098", "120.00"))
    pays.append(("2026-11-06", "INV-0004 en INV-0011", "999.00"))
    R.shuffle(pays)
    w("t5h_invoices", "files/invoices.csv", "invoice,customer,amount\n" + "".join(f"{a},{b},{c}\n" for a, b, c in inv))
    w("t5h_invoices", "files/payments.csv", "date,reference,amount\n" + "".join(f"{a},{b},{c}\n" for a, b, c in pays))
    w("t5h_invoices", "prompt.md", B.T5_PROMPT)
    return inv, pays


# ---------- E0 s4: letters, second complaint asks about timing (no refund push) ----------
S4_C2 = """Beste,

Bedankt voor het aanbod. Wanneer mag ik de nieuwe lamp voor bestelling NL-7731 verwachten?
Ik ben volgende week op reis, dus ik wil weten of iemand thuis moet zijn.

Koen Maes
"""


# ---------- E0 s5: FAQ document ----------
S5_PROMPT1 = """`vragen.txt` holds customer questions. Write `faq.md` that answers each of them.

Rules:
- Each entry is a question on its own line in bold (`**...?**`), followed on the next line by its answer, then a blank line.
- Entries are sorted alphabetically by question.
- Each answer has at most 25 words.
- Address the reader formally (u/uw), never je/jij/jouw.
- Never state a price, amount or percentage: refer to the price list at `winkel.be/prijzen` instead.
"""
S5_PROMPT2 = """New questions came in: see `nieuwe_vragen.txt`. Add them to `faq.md`, following the same rules as before.
"""
S5_Q1 = """Hoe lang duurt de levering?
Kan ik mijn bestelling annuleren?
Wat kost een extra garantiejaar?
Bieden jullie studentenkorting?
"""
S5_Q2 = """Wat kost verzending naar Nederland?
Kan ik in de winkel afhalen?
Hoeveel korting krijg ik bij grote bestellingen?
"""


def build_e0b():
    w("s4_letters", "files1/klacht1.txt", B.S3_C1)
    w("s4_letters", "files2/klacht2.txt", S4_C2)
    w("s4_letters", "prompt1.md", B.S3_PROMPT1)
    w("s4_letters", "prompt2.md", B.S3_PROMPT2)
    w("s5_faq", "files1/vragen.txt", S5_Q1)
    w("s5_faq", "files2/nieuwe_vragen.txt", S5_Q2)
    w("s5_faq", "prompt1.md", S5_PROMPT1)
    w("s5_faq", "prompt2.md", S5_PROMPT2)


def all_rows():
    """Deterministic: rebuilds the same data the files hold (graders call this)."""
    global R, WRITE
    R, WRITE = random.Random(2611252), False
    out = build_t1h(), build_t2h(), build_t5h()
    WRITE = True
    return out


if __name__ == "__main__":
    build_t1h(); build_t2h(); build_t5h()
    build_e0b()
    labels = json.loads((B.ROOT / "labels.json").read_text())
    labels.update({"t1h_tickets": "parallel", "t2h_expenses": "mixed", "t5h_invoices": "mixed",
                   "s4_letters": "sequential", "s5_faq": "parallel"})
    (B.ROOT / "labels.json").write_text(json.dumps(labels, indent=2) + "\n")
    print("built2")
