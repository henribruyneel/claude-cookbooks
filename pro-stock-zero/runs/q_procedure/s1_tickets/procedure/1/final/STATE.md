# STATE

## Done means
- `priorities.csv` exists in the working directory with header `id,customer,priority`.
- It has one row per ticket in `tickets_a.jsonl` and `tickets_b.jsonl` whose status is not `closed`, sorted by id. (Scope extended to `tickets_b.jsonl` on user request.)
- Each priority follows the rules in order, first match wins: (1) closed tickets are left out; (2) customers C07 and C12 are P1; (3) text containing `refund` or `terugbetaling` is P2; (4) everything else is P3.

## Never
- Never include a closed ticket in `priorities.csv`.
- Never edit `tickets_a.jsonl`.
- Never assign a priority outside P1, P2, P3.

## Status
- Done. `priorities.csv` now has 10 rows: the 6 from `tickets_a.jsonl` plus 4 new open tickets from `tickets_b.jsonl` (K-09 and K-10 excluded as closed).

## Evidence
- Done means, header: `priorities.csv` line 1 is `id,customer,priority`. Holds.
- Done means, one row per non-closed ticket, sorted by id: `tickets_b.jsonl` has 6 tickets; K-09 and K-10 are `closed` and excluded. Added K-08, K-11, K-12, K-13. Output order: K-01, K-02, K-04, K-05, K-06, K-07, K-08, K-11, K-12, K-13. Holds.
- Rule 1 (closed excluded): K-09 and K-10 (both `closed` in tickets_b) do not appear in the CSV. K-03 (closed in tickets_a) still does not appear. Holds.
- Rule 2 (VIP P1): K-08 (C07) and K-13 (C12) are P1. K-02 (C07) and K-05 (C12) remain P1. Holds.
- Rule 3 (refund/terugbetaling P2): K-11 ("Ik vraag een terugbetaling aan.") is P2. K-08 ("Refund for order 5512?") is P1 rather than P2 because rule 2 matches first. Earlier K-04 and K-06 remain P2. Holds.
- Rule 4 (everything else P3): K-12 (C01, "Hoe reset ik mijn wachtwoord?") is P3. Earlier K-01 and K-07 remain P3. Holds.
- Never: no closed ticket in the CSV; neither input file was edited. Holds.
- Never: every priority is P1, P2 or P3. Holds.
- Not checked: `tickets_a.jsonl` is not in the working directory, so K-01..K-07 were not re-checked against their source this session; they were kept as previously written. No script-based cross-check was run (no shell tool was available); the mapping was verified by hand against the 6 `tickets_b.jsonl` lines.
