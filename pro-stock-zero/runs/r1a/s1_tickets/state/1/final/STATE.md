# STATE

## Conditions
1. Tickets with status `closed` are excluded.
2. Tickets from customers C07 and C12 are P1 (VIP).
3. Non-VIP tickets whose text contains `refund` or `terugbetaling` are P2.
4. All other included tickets are P3.
5. Rules apply first match wins (VIP before refund before default).
6. `priorities.csv` has header `id,customer,priority`, one row per included ticket, sorted by id.

## Status
- `priorities.csv` written with 10 rows (K-03, K-09, K-10 excluded as closed; 13 input tickets total across `tickets_a.jsonl` and `tickets_b.jsonl`).
- This file reflects the final state of the work.

## Evidence
- Input `tickets_a.jsonl` has 7 ticket lines (K-01..K-07); line 8 is empty. `tickets_b.jsonl` has 6 ticket lines (K-08..K-13).
- Condition 1: K-03, K-09, K-10 are `closed` and are absent from `priorities.csv`.
- Condition 2: K-02 (C07), K-05 (C12), K-08 (C07), K-13 (C12) are P1.
- Condition 3: K-04 ("terugbetaling"), K-06 ("Refund please"), K-11 ("terugbetaling", C06) are P2. All non-VIP.
- Condition 4: K-01 (C03), K-07 (C04), K-12 (C01, "Hoe reset ik mijn wachtwoord?") are P3.
- Condition 5: VIP ticket K-08 contains "Refund" but is P1, so VIP rule takes precedence.
- Condition 6: `priorities.csv` first line is `id,customer,priority`; rows are K-01, K-02, K-04, K-05, K-06, K-07, K-08, K-11, K-12, K-13 in ascending id order.
