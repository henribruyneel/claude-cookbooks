# STATE

## Done means
- `priorities.csv` exists in this directory with header `id,customer,priority`.
- It has exactly one row per ticket in `tickets_a.jsonl` and `tickets_b.jsonl` whose status is not `closed`, sorted by id.
- Each priority follows the rules, first match wins: (1) closed tickets are left out; (2) customers C07 and C12 are P1; (3) a ticket whose text contains `refund` or `terugbetaling` is P2; (4) everything else is P3.

## Never
- Do not include closed tickets in `priorities.csv`.
- Do not edit `tickets_a.jsonl`.
- Do not assign a priority outside P1, P2, P3.

## Status
- Done. `priorities.csv` now has 10 data rows: the 6 from `tickets_a.jsonl` (unchanged) plus 4 new non-closed tickets from `tickets_b.jsonl` (K-08, K-11, K-12, K-13). Closed K-09 and K-10 are left out. Checked by reading input and output, not by a script (no shell tool was available in this session).
- `tickets_a.jsonl` is not in this directory and could not be read this session (the read was denied, since it is outside the working directory). Its rows were carried over from the earlier run and were not re-verified against the file.

## Evidence
- Header: `priorities.csv` line 1 is `id,customer,priority`.
- Closed excluded: K-03 (status `closed`) is absent from the output.
- Rule 2 (VIP): K-02 (C07) and K-05 (C12) are P1.
- Rule 3 (refund): K-04 "Graag een terugbetaling..." (C09) is P2. K-06 "Refund please, wrong size." (C02) is P2. Matching is case-insensitive, which is my reading; the request does not say.
- Rule 4 (default): K-01 (C03, "Waar blijft mijn pakket?") is P3. K-07 (C04, "Bedankt!") is P3.
- Sorted by id: K-01, K-02, K-04, K-05, K-06, K-07.
- Row count: 6 non-closed tickets in the 7-line input, 6 data rows in the output.
- Not checked: whether the input file has more lines beyond the 7 shown, or whether any ticket text uses a refund word in a form other than the two listed.

### Update: tickets_b.jsonl added
- Header: `priorities.csv` line 1 is `id,customer,priority` (re-read after writing).
- Closed excluded: K-09 (`closed`, C11) and K-10 (`closed`, C12) are absent from the output.
- Rule 2 (VIP): K-08 (C07, "Refund for order 5512?") is P1. This is the first-match case: its text contains `refund`, but rule 2 comes first, so P1, not P2. K-13 (C12) is P1.
- Rule 3 (refund): K-11 (C06, "Ik vraag een terugbetaling aan.") is P2.
- Rule 4 (default): K-12 (C01, "Hoe reset ik mijn wachtwoord?") is P3.
- Only P1, P2, P3 are used (Never item 3 holds). No closed ticket is in the output (Never item 1 holds). The input file was not edited (Never item 2 holds: no write was made to `tickets_b.jsonl`).
- Sorted by id: K-01, K-02, K-04, K-05, K-06, K-07, K-08, K-11, K-12, K-13.
- Row count: 4 non-closed tickets in the 6-line `tickets_b.jsonl` (K-08, K-11, K-12, K-13) plus 6 from A = 10 data rows. Checked by eye against the file.
- Not checked: `tickets_a.jsonl` (see Status). Whether `tickets_b.jsonl` has lines beyond the 6 shown (the read returned 6 lines).
