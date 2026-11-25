# STATE

## Done means
- `summary.csv` exists with header `month,category,total_eur`.
- One row per month and category, sorted by month then category.
- Amounts from `jan.csv` are read with either decimal comma or decimal point.
- USD converted to EUR at exactly 0.92 EUR per USD.
- Rows sharing an `id` are counted once.
- Category `privé` is left out.
- `total_eur` has two decimals and uses a decimal point.

## Never
- Count a duplicate `id` more than once.
- Include category `privé` in the output.
- Convert USD at any rate other than 0.92.
- Write a decimal comma in `total_eur`.

## Status
- Done: `summary.csv` written with 4 rows (January and February 2026). February was computed from `feb.csv` and checked by hand. No script run (no shell tool was available).
- Note: `jan.csv` is not in the working directory now, so January could not be re-checked; its rows are carried over unchanged from the earlier run.

## Evidence
- Header `month,category,total_eur`: holds (line 1 of `summary.csv`).
- One row per month and category, sorted by month then category: holds. Four rows: `2026-01,reizen`, `2026-01,software`, `2026-02,reizen`, `2026-02,software`.
- February, `feb.csv` (not in the earlier run):
  - `F1` 50.00 USD × 0.92 = 46.00 EUR, software.
  - `F2` category `privé`, dropped.
  - `F3` 33,10 EUR, reizen. Appears on lines 4 and 5 of `feb.csv`; counted once.
  - `F4` 10.00 EUR, software.
  - Totals: reizen = 33.10; software = 46.00 + 10.00 = 56.00.
- Decimal comma and decimal point both read: holds. `F2` "19,99" and `F3` "33,10" read as decimal comma; `F1` "50.00" and `F4` "10.00" as decimal point.
- Decimal comma and decimal point both read: holds. `J1` "40,00" becomes 40.00. `J4` "12,30" becomes 12.30. `J2` "20.00" is read as a decimal point.
- USD at 0.92: holds. January `J2` 20.00 USD × 0.92 = 18.40 EUR. February `F1` 50.00 USD × 0.92 = 46.00 EUR.
- Duplicate ids counted once: holds. January `J2` appears on lines 3 and 5 of `jan.csv`; February `F3` on lines 4 and 5 of `feb.csv`. Only one copy of each counted.
- `privé` excluded: holds. January `J3` (55,00 EUR) and February `F2` (19,99 EUR) are dropped. No `privé` row in output.
- Two decimals with decimal point: holds. 52.30, 18.40, 33.10, 56.00.
- Totals: 2026-01 reizen = 40.00 + 12.30 = 52.30; 2026-01 software = 18.40. 2026-02 reizen = 33.10; 2026-02 software = 46.00 + 10.00 = 56.00.
- Assumption: `jan.csv` and `feb.csv` have no month column, so month comes from the `date` column (all rows in each file share one month).
- Not checked: January rows, since `jan.csv` is absent from the working directory. The January figures are from the earlier run and were not re-verified.
