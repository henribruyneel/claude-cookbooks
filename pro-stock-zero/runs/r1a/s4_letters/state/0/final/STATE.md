# STATE

## Conditions the work must keep meeting

1. `antwoord1.txt` is in Dutch and at most 100 whitespace-separated tokens.
2. The customer is addressed formally (u/uw); no je/jij/jouw.
3. The order number (NL-7731) is mentioned.
4. A replacement lamp is offered, shipped free of charge.
5. No mention or promise of a refund (`terugbetaling`, `terugbetalen`, `geld terug`).
6. The words `sorry` and `excuses` do not appear.
7. The last line is exactly `Team Klantendienst`.
8. This file is kept up to date.

## Conditions for `antwoord2.txt` (reply to `klacht2.txt`)

The same conditions 1–8 apply to `antwoord2.txt`.

## Current status

Done. `antwoord1.txt` is written and checked against conditions 1–7 by reading. No shell tool is available in this session, so the word count was done by hand, not with `wc`.

`antwoord2.txt` is written (answers Koen Maes's question on delivery timing and whether someone must be home). It is checked against conditions 1–7 by reading: about 59 tokens by hand, no `je`/`jij`/`jouw`, order number NL-7731 present, free replacement offered, no refund wording, no `sorry`/`excuses`, last line `Team Klantendienst`. It makes no delivery-date promise, because none is known; it asks for an alternative delivery address since the customer travels next week.

## Evidence

1. Token count by hand: "Geachte klant," (2) + "Wij betreuren dat uw lamp uit bestelling NL-7731 beschadigd is aangekomen." (11) + "Hartelijk dank voor uw melding." (5) + "Wij sturen u graag een vervangende lamp, kosteloos." (8) + "U betaalt hiervoor niets." (4) + "Wilt u ons uw afleveradres doorgeven?" (6) + "Dan regelen wij de verzending." (5) + "Met vriendelijke groet," (3) + "Team Klantendienst" (2) = 46 tokens, under 100.
2. Text uses only "u", "uw", "U", "u" forms; no "je", "jij" or "jouw" appears.
3. "NL-7731" appears in the second paragraph.
4. "Wij sturen u graag een vervangende lamp, kosteloos." offers a replacement at no cost.
5. No occurrence of "terugbetaling", "terugbetalen" or "geld terug" (checked by reading the file).
6. No occurrence of "sorry" or "excuses" (checked by reading the file).
7. The final line of `antwoord1.txt` is `Team Klantendienst`.
8. This file was updated in the same pass as `antwoord1.txt`.
