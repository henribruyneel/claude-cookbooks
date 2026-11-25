# Conditions

Rules copied from the user's task instructions. No reasons were given for these rules.

## Session instructions

- Before starting any request, copy every rule, format, filter, rate and must / must-not it contains into CONDITIONS.md in the working folder, with the reason if given, so a later session without this conversation can follow them.
- At the start of every task, read CONDITIONS.md if it exists and follow it.

## Task: priorities.csv

- Input: `tickets_a.jsonl` (customer tickets).
- Output: `priorities.csv` with the header `id,customer,priority`, one row per ticket, sorted by id.
- Rules, first match wins:
  1. Leave out tickets with status `closed`.
  2. Customers `C07` and `C12` are VIP: their tickets are `P1`.
  3. A ticket that asks for a refund (`refund` or `terugbetaling`) is `P2`.
  4. Everything else is `P3`.

## Task: update priorities.csv with tickets_b.jsonl

- Request: new tickets arrived in `tickets_b.jsonl`. Update `priorities.csv` so it also covers them, following the same rules as before.
- Reason given: none.
- Interpretation: the same rules above apply to the tickets in `tickets_b.jsonl`; their rows are added to the existing `priorities.csv`, keeping the header and sorting by id.
- Rules: same as the "Task: priorities.csv" section above (closed tickets left out, VIP `C07`/`C12` → `P1`, refund/`terugbetaling` → `P2`, else `P3`; first match wins).
