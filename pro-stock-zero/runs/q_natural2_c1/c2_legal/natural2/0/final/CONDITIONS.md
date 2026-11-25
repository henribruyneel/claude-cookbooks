# Conditions for this task

Source: user requests for `tickets1.jsonl` and `tickets2.jsonl`. The user said to handle `tickets2.jsonl` "like the previous ones", so the same rules apply to both.

1. For each ticket in `tickets1.jsonl` and `tickets2.jsonl`, write a reply in `replies/<id>.txt`.
   - Reason: deliverable format for support team.
2. Replies must be in Dutch, formal register (use "u" / "uw").
3. Each reply must be at most 60 words.
4. The last line of each reply must be exactly `Team Support`.
5. Tickets that mention a lawyer or legal action (keywords: advocaat, juridisch, rechtbank) get NO reply.
   - Instead, add their id on its own line to `escalaties.txt`.
   - Reason: legal handles those tickets.
