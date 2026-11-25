# STATE

## Done means
- `summary.csv` exists with header `month,category,total_eur`
- One row per month and category, sorted by month then category
- USD converted to EUR at exactly 0.92 EUR per USD; decimal comma and decimal point both parsed
- Duplicate `id` rows counted once
- Category `privé` left out
- `total_eur` has two decimals and a decimal point

## Never
- Count a duplicate `id` twice
- Include category `privé` in any row
- Use a conversion rate other than 0.92 EUR per USD
- Modify `jan.csv`

## Status
- Done: `summary.csv` has header and 4 rows, now including February 2026 (`2026-02,reizen,33.10` and `2026-02,software,56.00`). All five Done means hold (see Evidence).

## Evidence
February (from `feb.csv`, 4 data rows F1–F4):
- Header and sort: `summary.csv` line 1 is `month,category,total_eur`; 2026-02 rows come after 2026-01 and `reizen` comes before `software` within the month. Holds.
- One row per month and category: 2026-02 has one `reizen` row and one `software` row. Holds.
- USD conversion: F1 is 50.00 USD × 0.92 = 46.00 EUR. Parsed the decimal point. Holds.
- Decimal comma parsed: F3 `33,10` = 33.10 EUR. Software = 46.00 (F1) + 10.00 (F4, `10.00` EUR) = 56.00. Holds.
- Duplicates: F3 appears twice in `feb.csv` (lines 4 and 5); counted once, so reizen = 33.10, not 66.20. Holds.
- `privé`: F2 (19,99 EUR) excluded; no `privé` row for 2026-02 in output. Holds.
- Two decimals with a decimal point: `33.10`, `56.00`. Holds.
- Never: `feb.csv` was only read. No duplicate double-counted, no privé row, rate 0.92 only. Holds.
- January rows are unchanged from the previous write (`52.30`, `18.40`). Their source `jan.csv` is not in this directory, so I could not re-check them against it in this session; I did not modify or read it.
- Not checked by script: totals were computed by hand from the four February rows, not by a parser run.
