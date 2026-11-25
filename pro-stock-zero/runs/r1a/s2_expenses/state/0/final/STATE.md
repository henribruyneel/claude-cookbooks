# STATE

## Conditions the work must keep meeting

1. `summary.csv` has the header `month,category,total_eur`.
2. One row per (month, category) pair, sorted by month, then category.
3. Amounts with a decimal comma or a decimal point are both parsed correctly.
4. USD is converted to EUR at exactly 0.92 EUR per USD.
5. Rows sharing an `id` are counted once.
6. Category `privé` is excluded.
7. `total_eur` has two decimals and uses a decimal point.

## Current status

Done. `summary.csv` is written with two rows for 2026-01 and two rows for 2026-02. Conditions 1–7 were checked by reading the source data and the output file.

February (`feb.csv`):
- F1, software, 50.00 USD → 46.00 EUR (50.00 × 0.92)
- F2, privé, 19,99 EUR → excluded
- F3, reizen, 33,10 EUR → 33.10 (appears twice with the same id; counted once)
- F4, software, 10.00 EUR → 10.00
- Totals: 2026-02/reizen 33.10; 2026-02/software 56.00

## Evidence

Source rows in `jan.csv`:
- J1, reizen, 40,00 EUR
- J2, software, 20.00 USD (appears twice; counted once)
- J3, privé, 55,00 EUR (excluded)
- J4, reizen, 12,30 EUR

1. Header in `summary.csv` is `month,category,total_eur`.
2. Rows are 2026-01/reizen then 2026-01/software (month, then category, alphabetical).
3. "40,00" → 40.00 and "12,30" → 12.30 (decimal comma); "20.00" → 20.00 (decimal point).
4. J2: 20.00 × 0.92 = 18.40 EUR.
5. J2 appears on lines 3 and 5 of `jan.csv` with the same id; included once.
6. J3 (privé) is not in the output.
7. reizen: 40.00 + 12.30 = 52.30; software: 18.40. Both printed with two decimals and a point.
