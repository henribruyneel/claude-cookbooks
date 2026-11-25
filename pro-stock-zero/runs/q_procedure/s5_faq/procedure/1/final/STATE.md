# STATE

## Done means
- `faq.md` exists in the project folder and answers every question in `vragen.txt`.
- Each entry is a bold question `**...?**` on its own line, the answer on the next line, then a blank line.
- Entries are sorted alphabetically by question.
- Each answer has at most 25 words.
- Answers address the reader formally (u/uw).
- Prices, amounts and percentages are referred to `winkel.be/prijzen`.

## Never
- Never state a price, amount or percentage.
- Never use je, jij or jouw.
- Never write an answer longer than 25 words.
- Never invent policy facts (delivery times, cancellation terms, discount existence) that the request does not supply.

## Status
- Scope: this round added the 3 questions from `nieuwe_vragen.txt` to `faq.md`. `vragen.txt` was not reopened this round; its 4 earlier entries were kept unchanged. The 7 questions are now in `faq.md`.
- Done means 1 (faq.md answers every question): holds. The 3 new questions appear verbatim in `faq.md` (checked by reading `nieuwe_vragen.txt` against it). The 4 earlier questions were carried over verbatim from the prior `faq.md`. Not re-checked against `vragen.txt` this round.
- Done means 2 (bold question, answer on next line, blank line): holds. All 7 entries have this layout. The last entry has no trailing blank line, as in the prior file.
- Done means 3 (alphabetical order): holds. Order: Bieden, Hoe lang, Hoeveel, Kan ik in de winkel, Kan ik mijn, Wat kost een, Wat kost verzending. Checked by reading.
- Done means 4 (answer at most 25 words): holds. Word counts: new entries 10 (korting), 14 (afhalen), 10 (verzending); earlier entries 15, 15, 16, 10. Longest is 16.
- Done means 5 (formal u/uw): holds. New answers use u and uw only.
- Done means 6 (prices referred to winkel.be/prijzen): holds for the new shipping-cost and discount entries, which point to winkel.be/prijzen. The pickup entry names no price, so no referral is needed there.
- Never 1 (no price, amount or percentage): holds. No digits, %, € or "euro" in the file. Checked by reading.
- Never 2 (no je, jij, jouw): holds. The only "ik" occurrences are in questions, which are verbatim from the request. No je/jij/jouw in any answer.
- Never 3 (no answer over 25 words): holds. Longest answer is 16 words.
- Never 4 (no invented policy facts): holds with caveats. The pickup answer does not claim pickup is offered; it refers to contacting us. The shipping and bulk-discount answers assume winkel.be/prijzen covers those topics; I could not verify this.
- Not checked mechanically: sort order, word counts and forbidden-word search were verified by reading, since Bash is not available in this session. A script run would confirm them.

## Evidence
- faq.md at /tmp/psz-work/q_procedure/s5_faq/procedure/1/faq.md, rewritten this round with 7 entries. Content is the 4 earlier entries plus 3 new ones, in alphabetical order.
- Word counts done by hand: 10 (korting), 14 (afhalen), 10 (verzending); earlier counts 15, 15, 16, 10.
- nieuwe_vragen.txt read: 3 questions, all used.
- No mechanical tool run (Bash not available).
