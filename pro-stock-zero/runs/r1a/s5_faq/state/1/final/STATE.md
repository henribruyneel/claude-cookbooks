# STATE

## Conditions the work must keep meeting

1. `faq.md` answers every question in `vragen.txt` (4 questions).
2. Each entry: question on its own line in bold (`**...?**`), answer on the next line, then a blank line.
3. Entries are sorted alphabetically by question.
4. Each answer has at most 25 words.
5. The reader is addressed formally (u/uw); no je/jij/jouw in answers.
6. No price, amount or percentage is stated; the reader is referred to `winkel.be/prijzen` instead.

## Current status

`faq.md` is written with 4 entries. Conditions 1–6 were checked by reading the file, because Bash is not available in this session, so no script ran. Open point: the answers to "Hoe lang duurt de levering?" and "Kan ik mijn bestelling annuleren?" contain no concrete facts, because no delivery or cancellation policy was provided. They need review by the business.

## Evidence that each condition holds

1. `vragen.txt` lists: Hoe lang duurt de levering? / Kan ik mijn bestelling annuleren? / Wat kost een extra garantiejaar? / Bieden jullie studentenkorting? — each has one entry in `faq.md`.
2. `faq.md` lines follow the pattern bold question, answer line, blank line, for all 4 entries.
3. Question order in `faq.md`: Bieden jullie studentenkorting? → Hoe lang duurt de levering? → Kan ik mijn bestelling annuleren? → Wat kost een extra garantiejaar? (B < H < K < W).
4. Word counts (manual): 17, 19, 19, 10 — all ≤ 25.
5. Answers use "u" / "uw" / "ons" / "wij"; none contains je, jij or jouw. The word "jullie" appears only in the customer's question text, copied verbatim from `vragen.txt`.
6. No digits, %, or € sign in `faq.md`; prices are referred to via `winkel.be/prijzen` in entries 1 and 4.
