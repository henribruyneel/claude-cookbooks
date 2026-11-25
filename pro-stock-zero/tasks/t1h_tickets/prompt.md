`tickets.jsonl` holds support tickets, one JSON object per line.

Write `priorities.csv` with the header `id,priority` and one row per ticket, sorted by id ascending.

Assign priority with these rules. The first rule that matches wins:
1. Tickets with status `closed` are left out of the file.
2. Tickets from an email address ending in `@acme-intern.be` get `P4`.
3. Plan `enterprise` and the subject or body mentions an outage → `P1`.
4. Any other plan and the subject or body mentions an outage → `P2`.
5. The subject or body mentions `invoice`, `factuur` or `refund` → `P3`.
6. Everything else → `P4`.

"Mentions an outage" means it contains one of: `down`, `outage`, `cannot log in`, `kan niet inloggen`, matched as whole words or whole phrases, case-insensitive. "Mentions invoice, factuur or refund" uses the same whole-word matching.
