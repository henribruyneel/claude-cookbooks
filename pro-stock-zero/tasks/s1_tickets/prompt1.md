`tickets_a.jsonl` holds customer tickets.

Write `priorities.csv` with the header `id,customer,priority`, one row per ticket, sorted by id.

Rules, first match wins:
1. Leave out tickets with status `closed`.
2. Customers `C07` and `C12` are VIP: their tickets are `P1`.
3. A ticket that asks for a refund (`refund` or `terugbetaling`) is `P2`.
4. Everything else is `P3`.
