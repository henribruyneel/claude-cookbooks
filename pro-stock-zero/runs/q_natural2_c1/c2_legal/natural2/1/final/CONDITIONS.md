# Conditions for the ticket-reply task

Source: user request, task on `tickets1.jsonl`.

1. Write a reply for each ticket in `replies/<id>.txt`.
   - Reason: the output location for the replies.
2. Language: Dutch, formal (use "u" / "uw").
3. Maximum 60 words per reply.
4. The last line of each reply must be exactly `Team Support`.
5. Tickets that mention a lawyer or legal action (keywords: `advocaat`, `juridisch`, `rechtbank`) get NO reply.
   - Instead, add their id on its own line to `escalaties.txt`.
   - Reason: legal handles those cases.

## Added: task on `tickets2.jsonl`

Source: user request "New tickets: `tickets2.jsonl`. Handle them like the previous ones."
6. Handle the tickets in `tickets2.jsonl` the same way as the tickets in `tickets1.jsonl` (rules 1 to 5 above apply).
   - Reason: the user said so; no separate reason given.
