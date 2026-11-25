# STATE

## Conditions the work must keep meeting

1. `priorities.csv` has the header `id,customer,priority`.
2. It has one row per ticket in `tickets_a.jsonl` that is not `closed`, and no other rows.
3. Rows are sorted by `id`.
4. Tickets with status `closed` are left out (rule 1).
5. Tickets from VIP customers `C07` and `C12` are `P1` (rule 2).
6. Non-VIP tickets whose text asks for a refund (`refund` or `terugbetaling`, matched case-insensitively) are `P2` (rule 3).
7. All other non-closed tickets are `P3` (rule 4).
8. Rules are applied in order, first match wins: a VIP ticket that also asks for a refund is `P1`.

## Current status

Done. `priorities.csv` is written with 10 rows (K-01, K-02, K-04, K-05, K-06, K-07 from `tickets_a.jsonl`; K-08, K-11, K-12, K-13 from `tickets_b.jsonl`). K-03, K-09 and K-10 are excluded because they are closed.

Added from `tickets_b.jsonl` (same rules):
- K-08 (C07, open, "Refund for order 5512?"): VIP → P1. Conditions 5, 8.
- K-09 (C11, closed): excluded. Condition 4.
- K-10 (C12, closed): excluded. Condition 4.
- K-11 (C06, open, "Ik vraag een terugbetaling aan."): not VIP, contains `terugbetaling` → P2. Condition 6.
- K-12 (C01, open, "Hoe reset ik mijn wachtwoord?"): not VIP, no refund term → P3. Condition 7.
- K-13 (C12, open, "Kan ik mijn bestelling nog aanpassen?"): VIP → P1. Conditions 5, 8.

## Evidence

Source: `tickets_a.jsonl` has 7 tickets.

- K-01 (C03, open, "Waar blijft mijn pakket?"): not VIP, no refund term → P3. Condition 7.
- K-02 (C07, open, "Kleine vraag over openingsuren."): VIP → P1. Conditions 5, 8.
- K-03 (C05, closed): excluded. Condition 4.
- K-04 (C09, open, "Graag een terugbetaling voor het defecte toestel."): not VIP, contains `terugbetaling` → P2. Condition 6.
- K-05 (C12, open, "Adres wijzigen aub."): VIP → P1. Conditions 5, 8.
- K-06 (C02, open, "Refund please, wrong size."): not VIP, contains `Refund` → P2. Condition 6.
- K-07 (C04, open, "Bedankt!"): not VIP, no refund term → P3. Condition 7.

Row count (6) equals the 7 tickets minus 1 closed ticket (condition 2). Sort order K-01, K-02, K-04, K-05, K-06, K-07 is ascending by id (condition 3). The header was written exactly as specified (condition 1).

Assumption: the refund match is case-insensitive, so `Refund` in K-06 counts. If it should be case-sensitive, K-06 would become P3.
