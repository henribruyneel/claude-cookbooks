# Conditions for this working folder

Rules copied from the user's request (task: write priorities.csv from tickets_a.jsonl).

## Output file: priorities.csv
- Header must be exactly: `id,customer,priority`
- One row per ticket.
- Sorted by id.

## Classification rules (first match wins)
1. Leave out tickets with status `closed`.
2. Customers `C07` and `C12` are VIP: their tickets are `P1`.
3. A ticket that asks for a refund (`refund` or `terugbetaling`) is `P2`.
4. Everything else is `P3`.

Reasons: none given by the user.

## Follow-up request: add tickets_b.jsonl
- Request: update `priorities.csv` so it also covers the new tickets in `tickets_b.jsonl`, "following the same rules as before".
- No new rules or reasons were given; the classification rules and output format above still apply.
- Sort order and header stay the same (`id,customer,priority`, sorted by id).

## Standing instructions (from session setup)
- Before starting any request, copy every rule, format, filter, rate, and must/must-not into this file, with the reason if given.
- At the start of every task, read CONDITIONS.md if it exists and follow it.
