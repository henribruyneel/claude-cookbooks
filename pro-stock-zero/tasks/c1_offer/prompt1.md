`prijzen.csv` is our price list, `bestelling1.csv` a customer order.

Write `offerte1.csv` with header `sku,aantal,excl,btw,incl`, one row per order line in order, then a last row `TOTAAL,,<sum excl>,<sum btw>,<sum incl>`.
- excl = price × quantity, minus 10% when the quantity is 10 or more.
- VAT is 6% for category `boek`, 21% for everything else.
- Round excl and btw per line to cents, half up; incl = excl + btw. Two decimals, decimal point.
