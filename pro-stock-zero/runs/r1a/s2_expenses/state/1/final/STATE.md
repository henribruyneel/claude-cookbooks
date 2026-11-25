# STATE

## Conditions the work must keep meeting

1. `summary.csv` exists in this folder with the header `month,category,total_eur`.
2. One row per month and category, sorted by month, then category.
3. Decimal comma and decimal point amounts in `jan.csv` are both parsed correctly.
4. USD is converted to EUR at exactly 0.92 EUR per USD.
5. Rows sharing the same `id` are counted once.
6. Category `privé` is excluded.
7. `total_eur` has two decimals and uses a decimal point.
8. `STATE.md` keeps these three sections: conditions, current status, evidence.

## Current status

`summary.csv` written with 4 rows (2026-01/reizen, 2026-01/software, 2026-02/reizen, 2026-02/software). Work is complete; no open items.

Source rows from `feb.csv` (header + 5 data rows):

| id | date | category | amount | currency | treatment |
|----|------|----------|--------|----------|-----------|
| F1 | 2026-02-02 | software | 50.00 | USD | counted: 50.00 x 0.92 = 46.00 EUR |
| F2 | 2026-02-05 | privé | 19,99 | EUR | excluded (category privé) |
| F3 | 2026-02-11 | reizen | 33,10 | EUR | counted once: 33.10 EUR (appears twice; second copy dropped) |
| F3 | 2026-02-11 | reizen | 33,10 | EUR | duplicate of F3, skipped |
| F4 | 2026-02-19 | software | 10.00 | EUR | counted: 10.00 EUR |

Feb totals: reizen = 33.10; software = 46.00 + 10.00 = 56.00.

## Evidence

Source rows from `jan.csv` (header + 5 data rows):

| id | date | category | amount | currency | treatment |
|----|------|----------|--------|----------|-----------|
| J1 | 2026-01-04 | reizen | 40,00 | EUR | counted: 40.00 EUR (decimal comma) |
| J2 | 2026-01-09 | software | 20.00 | USD | counted once: 20.00 x 0.92 = 18.40 EUR (appears twice; second copy dropped) |
| J2 | 2026-01-09 | software | 20.00 | USD | duplicate of J2, skipped |
| J3 | 2026-01-12 | privé | 55,00 | EUR | excluded (category privé) |
| J4 | 2026-01-20 | reizen | 12,30 | EUR | counted: 12.30 EUR (decimal comma) |

- Condition 1: `summary.csv` line 1 is `month,category,total_eur`.
- Condition 2: rows are `2026-01,reizen` then `2026-01,software`; only one month (2026-01) appears in the input, and "reizen" sorts before "software".
- Condition 3: "40,00" and "12,30" (decimal comma) and "20.00" (decimal point) were all read as the intended values.
- Condition 4: 20.00 USD x 0.92 = 18.40 EUR.
- Condition 5: J2 appears on lines 3 and 5 of `jan.csv` with identical content; it is counted once.
- Condition 6: J3 (privé) does not appear in `summary.csv`.
- Condition 7: totals are 52.30 (reizen = 40.00 + 12.30) and 18.40 (software); both have two decimals with a point.
- Condition 8: this file contains the three sections above.

Verification note: the shell tool was unavailable in this session, so the checks above were done by reading the files and recomputing the arithmetic by hand, not by running a script.
