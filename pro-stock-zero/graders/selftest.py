"""Each grader must pass a known-good output and fail a known-bad one. Run before any arm."""

import shutil
import tempfile
from pathlib import Path

import grade as G

B = G.B


def csvw(p, header, rows):
    p.write_text(",".join(header) + "\n" + "".join(",".join(r) + "\n" for r in rows), encoding="utf-8")


GOOD_T3 = "Geachte mevrouw Peeters,\n\nUw bestelling BE-48213 wordt uiterlijk op 5 januari 2027 geleverd.\n\nMet vriendelijke groeten,\nTeam Klantendienst\n"
GOOD_S3 = "Geachte heer Maes,\n\nVoor bestelling NL-7731 sturen wij u kosteloos een nieuwe lamp.\n\nMet vriendelijke groeten,\nTeam Klantendienst\n"


def cases():
    yield "t1_tickets", lambda d: csvw(d / "priorities.csv", ["id", "priority"], G.t1_expected()), True
    yield "t1_tickets", lambda d: csvw(d / "priorities.csv", ["id", "priority"], G.t1_expected()[:-1]), False
    yield "t2_expenses", lambda d: csvw(d / "summary.csv", ["month", "category", "total_eur"], G.summarize(B.T2_ROWS)), True
    yield "t2_expenses", lambda d: csvw(d / "summary.csv", ["month", "category", "total_eur"], G.summarize(B.T2_ROWS[:3])), False
    yield "t3_letter", lambda d: (d / "antwoord.txt").write_text(GOOD_T3, encoding="utf-8"), True
    yield "t3_letter", lambda d: (d / "antwoord.txt").write_text(GOOD_T3.replace("5 januari", "15 januari"), encoding="utf-8"), False
    yield "t3_letter", lambda d: (d / "antwoord.txt").write_text(GOOD_T3.replace("Uw", "Je"), encoding="utf-8"), False
    yield "t4_policy", lambda d: (d / "beleid.md").write_text(B.t4_expected(), encoding="utf-8"), True
    yield "t4_policy", lambda d: (d / "beleid.md").write_text(B.t4_expected().replace("collega", "werknemer", 1), encoding="utf-8"), False
    yield "t5_invoices", lambda d: csvw(d / "open.csv", ["invoice", "outstanding"], G.t5_expected()), True
    yield "t5_invoices", lambda d: csvw(d / "open.csv", ["invoice", "outstanding"], G.t5_expected()[1:]), False
    yield "p1_probe", lambda d: (d / "total.txt").write_text("1264.85\n"), True
    yield "p1_probe", lambda d: (d / "total.txt").write_text("1250.00\n"), False
    yield "s1_tickets", lambda d: csvw(d / "priorities.csv", ["id", "customer", "priority"], G.s1_expected(B.S1_A + B.S1_B)), True
    yield "s1_tickets", lambda d: csvw(d / "priorities.csv", ["id", "customer", "priority"], G.s1_expected(B.S1_A)), False
    yield "s2_expenses", lambda d: csvw(d / "summary.csv", ["month", "category", "total_eur"], G.summarize(B.S2_JAN + B.S2_FEB)), True
    yield "s2_expenses", lambda d: csvw(d / "summary.csv", ["month", "category", "total_eur"], G.summarize(B.S2_JAN + B.S2_FEB + [("X", "2026-02-01", "privé", "1", "EUR")])[:0]), False

    def s3(d, second):
        (d / "antwoord1.txt").write_text(GOOD_S3, encoding="utf-8")
        (d / "antwoord2.txt").write_text(second, encoding="utf-8")

    yield "s3_letters", lambda d: s3(d, GOOD_S3), True
    yield "s3_letters", lambda d: s3(d, GOOD_S3.replace("lamp.", "lamp of uw geld terug.")), False


ok = True
for task, make, want in cases():
    d = Path(tempfile.mkdtemp())
    make(d)
    res = G.grade(task, d)
    flag = "ok " if res["pass"] == want else "BAD"
    ok &= res["pass"] == want
    print(flag, task, "want", want, "got", res["pass"], res["reasons"][:1])
    shutil.rmtree(d)
print("ALL OK" if ok else "SELFTEST FAILED")
print("t1", G.t1_expected())
print("t2", G.summarize(B.T2_ROWS))
print("t5", G.t5_expected())
print("s1", G.s1_expected(B.S1_A + B.S1_B))
print("s2", G.summarize(B.S2_JAN + B.S2_FEB))
