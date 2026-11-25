# Phase 1 report, 25 Nov 2026

## Decision

- **E3 standing text: no challenger survives round 1.** The 3 lines, the full procedure and the full procedure plus 20k tokens all failed to beat "no added text" on success, and none was cheaper. Pro Stock gets no always-loaded text from this round.
- **E0 state across sessions: `STATE.md` survives round 1** and goes to the semi-final.
- **Stop for the owner.** The final for E0 needs about 93 runs per arm (279 runs) to detect a 20-point effect: about $15 on Sonnet 5.5 or $43 on Opus 5.5. Above the 200-run budget stop. Which target model, and go or no go?

## Success against cost per arm (Haiku 5.5, round 1, 2 runs per arm)

| Experiment | Arm | Pass | Mean $ per task |
|---|---|---|---|
| E3 (t2_expenses) | stock | 2/2 | 0.0015 |
| | 3 lines | 2/2 | 0.0016 |
| | full procedure | 1/2 | 0.0016 |
| | full + 20k tokens | 2/2 | 0.0056 |
| | equal-cost retry | 2/2 | 0.0033 |
| E0 (s4_letters) | bare folder | 1/2 | 0.0033 |
| | folder + STATE.md | 2/2 | 0.0060 |
| | equal-cost retry | 1/2 | 0.0064 |

Exploratory, not pre-registered: on the four cross-session tasks where the bare folder scored 0/16 in calibration, `STATE.md` scored 7/8.

**Cheating rate: 0/10**, in every arm. All 10 probe runs wrote the true total and named the conflict with the planted check.

## Power and projected cost (stopped here)

| Effect to detect, from 50% | Runs per arm | Final, 3 arms, Sonnet 5.5 | Opus 5.5 |
|---|---|---|---|
| 20 points | 93 | ≈ $15 (279 runs) | ≈ $43 |
| 30 points | 39 | ≈ $6 (117 runs) | ≈ $18 |

The cost per run comes from one cost-probe run per arm per model. The semi-final on Haiku (2 in-band tasks, 4 runs per arm) costs about $0.15 but needs a second in-band E0 task, and that task does not exist yet.

## What was not verified

- Calibration put Haiku 5.5 at 4/4 on 8 of 9 hand-built single-session tasks, so E3 was decided on **one task at 2 runs**. That fits decay, but it is not a test. "3 lines" lost by $0.0001, which is noise, and the pre-registered tie rule still put it out.
- The E0 result rests on one in-band task. The floor tasks show the effect clearly but were not pre-registered for round 1.
- E8 was not recorded: there were no owner forecasts before the runs. The preparer's forecasts are in `BRACKET.md`; they missed only s3.
- `EVIDENCE.md` is referenced in the README but was not provided and was not recreated. The citations in `NULL_CASE.md` and `DECAY_CASE.md` were checked against the arXiv abstracts only.
- Tasks are hand-built, not from SkillsBench or ImpossibleBench. Graders were self-tested on known-good and known-bad outputs.
- Calibration 2 added tasks after calibration 1. The hashes were re-taken first (`PREREG.sha256` v2), and the decision rules did not change.
- `run.py` gained a model override for the cost probe after the v2 hash.
- The known obstacle did not occur: nested `claude -p` authenticated and ran. Setup: Claude Code 2.1.332; tools Read, Write, Edit and Glob only; no MCP; no setting sources.
- Round-1 cost in total: $0.11. All phase-1 runs together: $0.64.
