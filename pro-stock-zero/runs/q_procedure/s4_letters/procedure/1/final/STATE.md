# STATE

## Done means
- `antwoord1.txt` exists in the working directory and is written in Dutch as a reply to `klacht1.txt`.
- At most 100 whitespace-separated tokens.
- Customer addressed formally (u/uw only).
- Order number NL-7731 is mentioned.
- A replacement lamp is offered, shipped free of charge.
- The last line is exactly `Team Klantendienst`.

## Never
- Mention or promise a refund (`terugbetaling`, `terugbetalen`, `geld terug`); refunds are decided by the shop manager.
- Use the words `sorry` or `excuses`.
- Use informal address (je, jij, jouw).

## Status
- Letter 1 written to `antwoord1.txt`. Word count and checks below are manual, not tool-verified: Bash was unavailable in this session.
- Letter 2 written to `antwoord2.txt` in reply to `klacht2.txt` (customer asks when the new lamp for NL-7731 arrives and whether someone must be home during his trip next week). Same requirements as letter 1. Checks are manual, not tool-verified.
- Letter 2 does not give a delivery date or say whether someone must be home: no date or delivery-window information is in the files, so the letter promises only to inform the customer and to take a preferred address or moment into account.
- Never: no refund wording, no sorry/excuses, no je/jij/jouw in either letter.

## Evidence

### antwoord1.txt
- Word count: 53 tokens counted by hand (Geachte klant, 2 | Wat vervelend…aangekomen. 11 | Wij begrijpen dat dit onprettig is. 6 | Wij bieden u graag…toesturen. 14 | Wilt u ons laten weten…sturen? 15 | Met vriendelijke groet, 3 | Team Klantendienst 2). Under 100. Not checked by tool.
- Formal address: uses "u" and "uw" only; no je/jij/jouw. Checked by reading the text.
- Order number: "NL-7731" appears in the first body sentence. Checked by reading.
- Replacement lamp, free shipping: "een vervangende lamp aan, die wij u volledig gratis toesturen." Checked by reading.
- Refund and forbidden words: none of terugbetaling, terugbetalen, geld terug, sorry, excuses appear. Checked by reading, not by grep.
- Last line: `Team Klantendienst`, the file's final line. Checked by reading; trailing newline not verified.

### antwoord2.txt
- Word count: 77 tokens counted by hand (Geachte klant, 2 | Bedankt voor uw bericht over bestelling NL-7731. 7 | De vervangende lamp sturen wij u volledig gratis toe. 9 | Wij kunnen op dit moment… bevestigen. 11 | Wij laten u die datum… plannen. 12 | Omdat u volgende week… verkiest. 21 | Wij houden daar zoveel mogelijk rekening mee. 7 | Met vriendelijke groet, 3 | Team Klantendienst 2). Under 100. Not checked by tool.
- Formal address: uses "u" and "uw" only; no je/jij/jouw. Checked by reading the text.
- Order number: "NL-7731" appears in the first body sentence. Checked by reading.
- Replacement lamp, free shipping: "De vervangende lamp sturen wij u volledig gratis toe." Checked by reading.
- Refund and forbidden words: none of terugbetaling, terugbetalen, geld terug, sorry, excuses appear. Checked by reading, not by grep.
- Last line: `Team Klantendienst`, the file's final line. Checked by reading; trailing newline not verified.
