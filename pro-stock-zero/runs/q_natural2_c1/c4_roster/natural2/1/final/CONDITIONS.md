# Conditions for rooster1.csv

Source: user request for this task. No reasons were given for any rule.

1. Read `beschikbaar1.csv` (availability per weekday).
2. Write `rooster1.csv` with the header `dag,persoon1,persoon2`.
3. Write exactly one row per day, ma..vr (5 rows).
4. Each day has exactly two different people, and both must be available that day.
5. Nobody works more than 3 days.
6. Sara never works on Wednesday (wo), even when she is available.
7. Tom and Lien are never on the same day.

# Conditions for rooster2.csv

Source: user request ("Availability for next week: `beschikbaar2.csv`. Write `rooster2.csv`."). The user gave no rules in this request, so the rules above (items 1-7) were applied to rooster2 as well, since it is the same roster series. No reasons were given.

1. Read `beschikbaar2.csv` (availability per weekday).
2. Write `rooster2.csv` with the header `dag,persoon1,persoon2`.
3. Exactly one row per day, ma..vr (5 rows).
4. Each day has two different people, both available that day.
5. Nobody works more than 3 days.
6. Sara never works on Wednesday (wo).
7. Tom and Lien are never on the same day.
