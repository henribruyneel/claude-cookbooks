# STATE

## Conditions (must keep holding)
1. `antwoord1.txt` is a Dutch reply to `klacht1.txt`.
2. At most 100 whitespace-separated tokens.
3. Formal address only (u/uw); no je/jij/jouw.
4. Mentions order number NL-7731.
5. Offers a replacement lamp, shipped free of charge.
6. No refund mention/promise (`terugbetaling`, `terugbetalen`, `geld terug`).
7. No `sorry` or `excuses`.
8. Last line is exactly `Team Klantendienst`.

## Status
Done. `antwoord1.txt` written (addressed to Koen Maes, the customer in `klacht1.txt`).

## Evidence
1. Text is in Dutch and answers the broken-lamp complaint.
2. Manual count of tokens: 49 (≤ 100). No shell was available to run `wc -w`, so this count was done by hand.
3. Uses "uw lamp", "bij u", "sturen u", "Wilt u"; no je/jij/jouw (checked by reading the text).
4. "(bestelling NL-7731)" appears in the first paragraph.
5. "Wij sturen u graag kosteloos een nieuwe vervanglamp toe; de verzending is volledig gratis."
6. None of the refund terms appear in the text.
7. Neither `sorry` nor `excuses` appears.
8. The final line of the file is `Team Klantendienst` (followed only by a newline).

## Round 2
Done. `antwoord2.txt` answers `klacht2.txt` (Koen Maes asks about the delivery date and whether someone has to be home, since they're travelling next week). It meets the same conditions 1–8, applied to klacht2.
- Tokens: 79, counted by hand (no shell available).
- Formal address only: "uw bericht", "Bent u", "Laat u", "geeft u".
- NL-7731 appears in the first paragraph. The free replacement is restated, and there is no refund wording and no sorry/excuses.
- No delivery date or courier details were made up (we don't have them). Instead the reply promises to share the expected date when the lamp ships, and offers to time the delivery around the trip or send it to another address.
