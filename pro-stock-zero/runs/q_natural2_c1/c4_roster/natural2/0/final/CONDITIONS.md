# Conditions for the roster task

Source: user request for `rooster1.csv`, built from `beschikbaar1.csv`. No reasons were given for these rules.

Follow-up request for `rooster2.csv` from `beschikbaar2.csv` ("Availability for next week"). The user did not restate rules, so the same rules below are carried over as the working assumption. Reason: the request is a repeat of the same task for the next week.

1. Write `rooster1.csv` with the header `dag,persoon1,persoon2`. For `rooster2.csv`, use the same header.
2. Write one row per day, ma through vr (ma, di, wo, do, vr).
3. Each day has exactly two different people, and both must be available that day according to the matching availability file (`beschikbaar1.csv` or `beschikbaar2.csv`).
4. Nobody works more than 3 days in the week.
5. Sara never works on wo (Wednesday), even when she is available.
6. Tom and Lien are never on the same day.
