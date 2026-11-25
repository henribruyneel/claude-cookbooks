# Conditions for this task

Rules from the user's request (kept so later sessions can follow them):

- Input file: `jan.csv` lists January expenses.
- Output file: write `summary.csv` with the header `month,category,total_eur`.
  - Reason: format required by the user.
- One row per month and category, sorted by month, then category.
- Amounts may use a decimal comma or a decimal point.
- Convert USD to EUR at exactly 0.92 EUR per USD.
- Rows with the same `id` are duplicates: count each id once.
- Leave out the category `privé`.
- `total_eur` has two decimals and a decimal point.
