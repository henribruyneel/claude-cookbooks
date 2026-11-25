# Conditions for building offerte1.csv

Source request rules (no reasons were given for any of them):

Second request (`bestelling2.csv` -> `offerte2.csv`): "Make `offerte2.csv` the same way." All rules above apply unchanged, with `bestelling2.csv` as the order file and `offerte2.csv` as the output file.

- Input: `prijzen.csv` is the price list, `bestelling1.csv` is a customer order.
- Output file: `offerte1.csv`.
- Header must be exactly: `sku,aantal,excl,btw,incl`.
- One row per order line, in the same order as the order file.
- Final row must be: `TOTAAL,,<sum excl>,<sum btw>,<sum incl>`.
- excl = price × quantity, minus 10% when quantity is 10 or more.
- VAT is 6% for category `boek`, 21% for every other category.
- Round excl and btw per line to cents, half up.
- incl = excl + btw.
- All amounts have two decimals, using a decimal point.
