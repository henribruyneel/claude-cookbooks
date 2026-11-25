`jan.csv` lists January expenses.

Write `summary.csv` with the header `month,category,total_eur`, one row per month and category, sorted by month then category.

Rules:
- Amounts may use a decimal comma or a decimal point.
- Convert USD to EUR at exactly 0.92 EUR per USD.
- Rows with the same `id` are duplicates: count each id once.
- Leave out the category `privé`.
- `total_eur` has two decimals and a decimal point.
