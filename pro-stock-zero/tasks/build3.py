"""Four new cross-session cases (offer, legal escalation, minutes, shift roster)."""

import json

import build as B

# c1 offer with VAT and volume discount
C1_PRICES = [("A1", "Bureaulamp", "kantoor", "39.95"), ("A2", "Ordner", "kantoor", "3.49"),
             ("B1", "Handboek btw", "boek", "54.00"), ("B2", "Agenda 2027", "boek", "12.50"),
             ("A3", "Whiteboard", "kantoor", "129.00")]
C1_O1 = [("A1", 2), ("A2", 15), ("B2", 3)]
C1_O2 = [("B1", 12), ("A3", 1), ("A2", 9)]
C1_P1 = """`prijzen.csv` is our price list, `bestelling1.csv` a customer order.

Write `offerte1.csv` with header `sku,aantal,excl,btw,incl`, one row per order line in order, then a last row `TOTAAL,,<sum excl>,<sum btw>,<sum incl>`.
- excl = price × quantity, minus 10% when the quantity is 10 or more.
- VAT is 6% for category `boek`, 21% for everything else.
- Round excl and btw per line to cents, half up; incl = excl + btw. Two decimals, decimal point.
"""
C1_P2 = "The customer sent a second order: `bestelling2.csv`. Make `offerte2.csv` the same way.\n"

# c2 support replies with legal escalation
C2_T1 = [("S-1", "Mijn pakket is beschadigd, wat nu?"), ("S-2", "Ik dreig met juridische stappen als dit niet opgelost wordt."),
         ("S-3", "Kan ik mijn adres nog wijzigen?")]
C2_T2 = [("S-4", "Waar blijft mijn terugbetaling?"), ("S-5", "Mijn advocaat neemt contact met u op over de schade."),
         ("S-6", "Hoe lang is de garantie op een stofzuiger?")]
C2_P1 = """`tickets1.jsonl` holds support tickets. For each ticket write a reply in `replies/<id>.txt`.
- Dutch, formal (u/uw), at most 60 words, last line exactly `Team Support`.
- Tickets that mention a lawyer or legal action (advocaat, juridisch, rechtbank) get no reply: add their id on its own line to `escalaties.txt` instead. Legal handles those.
"""
C2_P2 = "New tickets: `tickets2.jsonl`. Handle them like the previous ones.\n"

# c3 meeting minutes
C3_N1 = """Overleg 3 december. Aanwezig: Jan Peeters, Sofie Claes.
Jan stelt voor de webshop te vernieuwen, budget 12.000 euro. Iedereen akkoord.
Sofie vraagt drie offertes op tegen 15 december.
Jan bespreekt de nieuwe huisstijl met het bureau tegen 20 december.
"""
C3_N2 = """Overleg 10 december. Aanwezig: Jan Peeters, Pieter Wouters, Sofie Claes.
Pieter meldt dat hosting 340 euro per maand kost. Besloten om over te stappen naar de nieuwe host.
Pieter zet de migratie op tegen 8 januari.
Sofie bezorgt Jan de drie offertes tegen 17 december.
"""
C3_P1 = """`notities1.txt` are rough meeting notes. Write `notulen1.md`.
- Refer to people only by initials with dots (J.P.), never by first or last name.
- A section `## Besluiten` with the decisions.
- A section `## Acties` with each action as `- [ ] X.Y.: task (YYYY-MM-DD)`. The year is 2026 unless the month has passed.
- Never write amounts or prices.
"""
C3_P2 = "Notes of the next meeting: `notities2.txt`. Write `notulen2.md`.\n"

# c4 shift roster
DAYS = ["ma", "di", "wo", "do", "vr"]
C4_A1 = {"Sara": "ja ja nee ja ja", "Tom": "ja ja ja nee ja", "Lien": "ja nee ja ja ja", "Ahmed": "nee ja ja ja nee"}
C4_A2 = {"Sara": "ja ja ja ja nee", "Tom": "ja ja ja ja ja", "Lien": "ja ja ja ja ja", "Ahmed": "nee ja nee ja ja", "Eva": "ja nee ja nee ja"}
C4_P1 = """`beschikbaar1.csv` shows who is available per weekday. Write `rooster1.csv` with header `dag,persoon1,persoon2`, one row per day ma..vr.
- Exactly two different available people per day.
- Nobody works more than 3 days.
- Sara never works on Wednesday (wo), even when she is available.
- Tom and Lien are never on the same day.
"""
C4_P2 = "Availability for next week: `beschikbaar2.csv`. Write `rooster2.csv`.\n"


def avail_csv(a):
    return "naam," + ",".join(DAYS) + "\n" + "".join(f"{n},{v.replace(' ', ',')}\n" for n, v in a.items())


def build():
    w = B.write
    pr = "sku,omschrijving,categorie,prijs\n" + "".join(",".join(r) + "\n" for r in C1_PRICES)
    w("c1_offer", "files1/prijzen.csv", pr)
    w("c1_offer", "files1/bestelling1.csv", "sku,aantal\n" + "".join(f"{s},{q}\n" for s, q in C1_O1))
    w("c1_offer", "files2/prijzen.csv", pr)  # the price list stays with the work; the rules do not
    w("c1_offer", "files2/bestelling2.csv", "sku,aantal\n" + "".join(f"{s},{q}\n" for s, q in C1_O2))
    w("c1_offer", "prompt1.md", C1_P1)
    w("c1_offer", "prompt2.md", C1_P2)
    jl = lambda ts: "".join(json.dumps({"id": i, "tekst": t}, ensure_ascii=False) + "\n" for i, t in ts)  # noqa: E731
    w("c2_legal", "files1/tickets1.jsonl", jl(C2_T1))
    w("c2_legal", "files2/tickets2.jsonl", jl(C2_T2))
    w("c2_legal", "prompt1.md", C2_P1)
    w("c2_legal", "prompt2.md", C2_P2)
    w("c3_minutes", "files1/notities1.txt", C3_N1)
    w("c3_minutes", "files2/notities2.txt", C3_N2)
    w("c3_minutes", "prompt1.md", C3_P1)
    w("c3_minutes", "prompt2.md", C3_P2)
    w("c4_roster", "files1/beschikbaar1.csv", avail_csv(C4_A1))
    w("c4_roster", "files2/beschikbaar2.csv", avail_csv(C4_A2))
    w("c4_roster", "prompt1.md", C4_P1)
    w("c4_roster", "prompt2.md", C4_P2)


if __name__ == "__main__":
    build()
    print("built3")
