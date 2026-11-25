`invoices.csv` lists invoices; `payments.csv` lists bank payments.

Write `open.csv` with the header `invoice,outstanding`: one row for each invoice that is not fully paid, sorted by invoice, with the outstanding amount (amount minus everything paid on it) with two decimals and a decimal point.

Matching rules:
- A payment belongs to an invoice when its reference contains that invoice's number, written in any form (`INV-0003`, `inv 3`, `Factuur 0003`, `INV0003` all mean invoice INV-0003).
- A payment whose reference names two invoices pays the first invoice in full and the rest goes to the second.
- Ignore payments whose reference names no existing invoice number.
- Overpayment on an invoice is not carried to other invoices; that invoice is simply not open.
