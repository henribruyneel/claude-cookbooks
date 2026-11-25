# STATE

## Done means
- `faq.md` exists in this directory and has one entry for each of the 4 questions in `vragen.txt`.
- Each entry is the question in bold (`**...?**`), then the answer on the next line, then a blank line.
- Entries are sorted alphabetically by question.
- Each answer has at most 25 words.
- Answers address the reader formally (u/uw) and never use je/jij/jouw.
- No answer states a price, amount or percentage; price questions refer to `winkel.be/prijzen`.

## Never
- Invent facts (delivery times, cancellation terms, warranty prices, discounts) that are not in the provided material.
- Put a price, amount, percentage or any digit in an answer.
- Use je, jij or jouw in an answer.
- Change the questions in `vragen.txt`.

## Status
- Done: `faq.md` now has 7 entries: the 4 from `vragen.txt` plus the 3 from `nieuwe_vragen.txt` (shipping cost, in-store pickup, bulk discount). Checked by reading the file; no shell tool was available, so no script was run.
- Open: the answers to delivery time, cancellation, pickup and bulk discount are routing answers, not facts. The source material did not include the actual terms, so they point the customer to contact or to `winkel.be/prijzen`. The student-discount answer does not confirm a discount exists.
- Note: the "Done means" section still says 4 questions from `vragen.txt`. The 3 new questions were added on the user's instruction; that section was not changed.

## Evidence
- Exists: `faq.md` is in this directory.
- One entry per question: 4 questions in `vragen.txt` and 3 in `nieuwe_vragen.txt` make 7; `faq.md` has 7 entries (studentenkorting, levering, bulkkorting, afhalen, annuleren, garantiejaar, verzending).
- Format: each question is bold and ends in `?`, the answer is on the next line, and a blank line follows each entry. Read by eye; the file ends with a blank line after the last entry.
- Sorted: Bieden, Hoe lang, Hoeveel, Kan ik in, Kan ik mijn, Wat kost een, Wat kost verzending. Checked by hand.
- At most 25 words: 12, 14, 13, 10, 10, 11 and 13 words for the seven entries, counted by hand. The new answers are 10, 13 and 10 words.
- Formal address: only u/uw is used. No je, jij or jouw appears (checked by reading).
- No price, amount, percentage or digit: none appears in the answers. The price-type questions (garantiejaar, verzending, bulkkorting) refer to `winkel.be/prijzen`. Treating the bulk discount as a price question is my choice.
- Not checked: whether the answers are factually correct. The material gave no delivery, cancellation, pickup, shipping, warranty or discount terms. The "Done means" word count and format were checked by reading, not by a script.
