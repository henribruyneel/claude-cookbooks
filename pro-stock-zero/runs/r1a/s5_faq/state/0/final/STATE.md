# STATE

## Conditions the work must keep meeting

1. `faq.md` answers every question in `vragen.txt`.
2. Each entry is a bold question `**...?**` on its own line, then the answer on the next line, then a blank line.
3. Entries are sorted alphabetically by question.
4. Each answer has at most 25 words.
5. Answers address the reader formally (u/uw) and never use je/jij/jouw.
6. No price, amount or percentage is stated; the reader is referred to `winkel.be/prijzen` instead.

## Current status

`faq.md` now holds all seven questions: the four from `vragen.txt` and the three from `nieuwe_vragen.txt`. All six conditions were checked by reading the file. Bash is disabled in this session, so the checks were manual, not scripted.

- Entries: 7 of 7 questions (4 from `vragen.txt`, 3 from `nieuwe_vragen.txt`).
- Order: Bieden, Hoe, Hoeveel, Kan ik in, Kan ik mijn, Wat kost een, Wat kost verzending (alphabetical).
- New answers: manual word counts 11 (discount), 16 (pickup), 10 (shipping). All are at most 25. Price and discount questions refer to `winkel.be/prijzen`. The in-store pickup answer is a general referral, as the source gives no policy.
- Open point: the answers on delivery time, cancellation and student discount are general referrals. The source material gives no facts on these, so no policy was invented. Replace them with the real policy if you have it.

## Evidence that each condition holds

1. The four questions in `vragen.txt` (Hoe lang duurt de levering?, Kan ik mijn bestelling annuleren?, Wat kost een extra garantiejaar?, Bieden jullie studentenkorting?) each have an entry in `faq.md`.
2. `faq.md` uses the layout `**Question?**` / answer / blank line for all four entries.
3. Sort order in `faq.md`: "Bieden…" < "Hoe…" < "Kan…" < "Wat…".
4. Manual word counts of the answers: 10, 17, 16, 13. All are at most 25.
5. Read-through of `faq.md`: no je, jij or jouw. Answers use "u" and "uw" ("uw bestelling", "vindt u", "raadpleegt u").
6. Read-through of `faq.md`: no digits, currency signs, "%" or "euro". The price question refers to `winkel.be/prijzen`.
