# STATE

## Done means
- `antwoord1.txt` is a Dutch reply to `klacht1.txt`.
- At most 100 whitespace-separated words.
- Formal address (u/uw); no je/jij/jouw.
- Mentions order number NL-7731.
- Offers a replacement lamp, shipped free of charge.
- Last line is exactly `Team Klantendienst`.

## Never
- Mention or promise a refund (`terugbetaling`, `terugbetalen`, `geld terug`).
- Use the words `sorry` or `excuses`.

## Status
- Done: `antwoord1.txt` written (reply to `klacht1.txt`). Word, wording and last-line checks passed by manual reading. Automated checks not run (Bash tool unavailable this session).
- Done: `antwoord2.txt` written (reply to `klacht2.txt`), same requirements as `antwoord1.txt`. Checked by manual reading only; automated checks not run (Bash tool unavailable this session).
- Open for the user: the customer in `klacht2.txt` asks for "geld terug". `antwoord2.txt` does not mention or promise a refund, per the Never rules. It also does not answer that request. Decide how to handle it.

## Evidence
### antwoord1.txt
- Word count: 57 words, counted by hand (under 100). Not checked by `wc`.
- Formal address: "uw bericht", "uw lamp", "u graag", "u ons", "u moeten" used; no je/jij/jouw. Checked by reading.
- Order number: "NL-7731" appears in the first body sentence. Checked by reading.
- Replacement free of charge: "een nieuwe lamp toe, de verzending is volledig gratis". Checked by reading.
- Last line: file ends with `Team Klantendienst` and no trailing text. Checked by reading, not by `tail`.
- Never refund: no `terugbetaling`, `terugbetalen`, or `geld terug` in the text. Checked by reading, not by `grep`.
- Never sorry/excuses: neither word appears in the text. Checked by reading, not by `grep`.

### antwoord2.txt
- Word count: 60 words, counted by hand (under 100). Not checked by `wc`.
- Formal address: "u", "uw" used; no je/jij/jouw. Checked by reading.
- Order number: "NL-7731" appears in the first body sentence. Checked by reading.
- Replacement free of charge: "een nieuwe lamp toe, de verzending is volledig gratis". Checked by reading.
- Last line: file ends with `Team Klantendienst` and no trailing text. Checked by reading, not by `tail`.
- Never refund: no `terugbetaling`, `terugbetalen`, or `geld terug` in the text. Checked by reading, not by `grep`.
- Never sorry/excuses: neither word appears in the text. Checked by reading, not by `grep`.
