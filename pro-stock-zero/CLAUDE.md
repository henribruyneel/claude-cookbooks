# Pro Stock Zero

- Files listed in `PREREG.sha256` (README sections 2 and 5, `arms/*`, `graders/grade.py`, `graders/selftest.py`) are pre-registered. No code checks the hashes, so an edit breaks the pre-registration silently. Change them only by writing a new `PREREG` version before the next run.
- Runs work in `psz-work` under the system temp dir (`WORKROOT` in `run.py`), outside the repo, so this file never reaches the arms. Keep it that way.
