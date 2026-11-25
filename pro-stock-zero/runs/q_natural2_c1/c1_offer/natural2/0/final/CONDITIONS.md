# Conditions for this working folder

Copied from the user's request. No reasons were given for these rules.

## Task: build offerte1.csv from prijzen.csv and bestelling1.csv

- Input files: `prijzen.csv` is the price list, `bestelling1.csv` is a customer order.
- Output file: `offerte1.csv`.
- Header must be exactly: `sku,aantal,excl,btw,incl`
- One row per order line, in the same order as the order file.
- Last row must be: `TOTAAL,,<sum excl>,<sum btw>,<sum incl>`
- excl = price × quantity, minus 10% when the quantity is 10 or more.
- VAT rate is 6% for category `boek`, and 21% for everything else.
- Round excl and btw per line to cents, half up.
- incl = excl + btw.
- Format: two decimals, decimal point (not comma).

## Task: build offerte2.csv from prijzen.csv and bestelling2.csv

- Same procedure and rules as offerte1.csv above ("make it the same way").
- Input: `bestelling2.csv` is the customer order. Output: `offerte2.csv`.
