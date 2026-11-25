`expenses.csv` lists business expenses.

Write `summary.csv` with the header `month,category,total_eur`: one row per month and category that has expenses, sorted by month and then category (alphabetical).

Rules:
- `month` is `YYYY-MM`.
- Amounts may use a decimal comma (`45,20`) or a decimal point (`29.00`). Negative amounts are refunds and count as negative.
- Convert USD to EUR at exactly 0.92 EUR per USD.
- Rows with the same `id` are duplicates: count each id once.
- Leave out the category `privé` entirely.
- `total_eur` has exactly two decimals with a decimal point. Round only the final total, half up.
