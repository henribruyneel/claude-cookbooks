## Pro Stock Zero, version 3

This file is all you need to start. Version 3 is version 2 after an adversarial pass against published work and a first bracket of cheap tests on 25 Nov 2026. Those tests chose this file's shape and reshaped experiment E0. Their numbers are in `EVIDENCE.md`.

---

# 1. Purpose

Modern agent practice is described as a stack: prompt, context, harness, loop, graph. Version 1 asked whether a deeper unit of optimisation explains that stack.

The published record changes the question. Each layer has already been shown to help in some conditions and to hurt in others. So a useful theory is one that **predicts in advance when a layer helps and when it hurts**, on tasks and setups it has not seen. Explaining the stack after the fact is not enough.

The practical use of the answer: one rule that decides what goes into "Pro Stock" (the owner's operating procedure for Claude Code and the Claude apps) and what is refused. This is the preparer's reading of the owner's goal, not confirmed by the owner.

---

# 2. Research question

Which measurable properties of a task and a setup predict whether adding a reference, a check, external state, standing context, or more agents will help or hurt?

And: does one quantity predict all five better than a predictor built from the layers themselves?

## Null hypothesis, steelmanned

Harness, Loop and Graph are the right units. What decides their effect is task structure (parallel or sequential) and model capability, as Kim et al. found across 180 configurations, with a predictor that chose the best architecture for 87% of held-out cases. No deeper unit is needed.

## Alternative hypothesis, steelmanned

Every layer works through one thing: reliable feedback from outside the worker. A layer helps when it raises the amount of trustworthy external feedback per step, and hurts when it adds context or coordination without it. The unit is the **checked step**: one change of persistent state plus one check, against a stated reference, that the worker did not write and cannot edit.

## Rival hypothesis: decay

Whatever a procedure adds is temporary. Gains shrink as models get stronger, and working practices get absorbed into the tools. The unit that matters is the model plus its default harness.

## Challenger hypothesis: the overruled loop

Any loop that optimises a measure it can see will, given enough rounds, move the measure without moving what the measure stands for. It keeps working only while something it cannot influence is allowed to overrule it: a check it cannot see or edit, replaced often enough that it cannot be learned, or a human decision. The checked step is the one-round case. This hypothesis adds two claims: a check that stays fixed is itself learned over rounds, and the reference can be wrong as well as missed. It says nothing about single-pass work, where there is no loop. Entered 25 Nov 2026, untested.

A hypothesis wins only by out-predicting the others on held-out configurations (experiment E7).

---

# 3. What the published record already teaches

The findings and their sources are in `EVIDENCE.md`. Open it only when a decision needs them. In one line each: always-loaded instructions can lower success and raise cost; rules a model writes for itself need a gate; more agents help parallel work and hurt sequential work; visible checks get gamed; what people feel about speed is not evidence; correction needs feedback from outside the worker.

---

# 4. Definitions

A task has a **reference**: the checks the owner accepts as meaning done. A **check** is a command's exit code, a quoted file, a count, or a named human decision. **State** is what persists between steps. A **step** is one action that changes state.

| Term | Definition | Measure |
|---|---|---|
| Breadth | What the model must hold or choose among, kept as separate counts | Standing context tokens; instructions always loaded; tools, skills and agents available; agents used |
| Depth | Independent checks an output survived that it could have failed | Checks that fail on a known-bad output and pass on this one |
| Quality | What the output does to the future | Held-out pass rate, paired with follow-up messages needed and with cheating rate |
| Iteration cost | What the result cost | Dollars and tokens first; steps and wasted steps second. Drop step counts if they correlate above 0.9 with tokens |
| Cheating rate | How often an arm passes a task whose visible check contradicts its instructions | Pass rate on impossible-task probes. The right behaviour is to report the conflict |
| Task structure | Whether the work splits into independent parts | Labelled per task before any run: parallel, sequential, or mixed |

As mathematics, Input → Output and State → State are the same function. As instructions to a worker they are different treatments: one asks for an answer to each request, the other asks that a set of conditions stay true. A first screen found no gain from the second inside one session, at about a quarter more tokens. Across sessions, a folder that carried its conditions did slightly better than one whose request history was gone. E0 now tests only that.

---

# 5. Experiments

Every experiment includes a stock arm and an equal-cost retry arm (stock, allowed to retry until it has spent what the treatment arm spent).

| ID | Arms | Kill condition for the alternative hypothesis |
|---|---|---|
| E0 State across sessions | A second session that starts with only the output files; a second session whose folder also carries `STATE.md` (conditions, status, evidence) | The state file does not beat the bare folder on held-out checks, or costs more for the same result |
| E3 Standing text | No added text; 3 lines; the full procedure; the full procedure plus 20k irrelevant tokens | The full procedure does not beat 3 lines on success at equal cost |
| E1 Reference | Stock; always write done and its check first; ask the owner only when the task is underspecified. Run on well-specified and underspecified versions of each task, with a scripted owner who holds the full specification | "Ask when underspecified" does not beat "always" on underspecified tasks, or costs success on well-specified ones |
| E2 Check | No check; worker-written check; hidden script check; model reviewer | Model reviewer matches the hidden script on held-out pass rate, or the hidden script raises the cheating rate |
| E5 Strength | E1 and E2 on a weaker and a stronger model | Gains vanish on the stronger model: decay wins |
| E6 Self-written rules | No rules; rules the model wrote after earlier tasks; the same rules admitted only after beating the current version | Gated rules do no better than ungated ones |
| E7 Prediction | Fit each hypothesis's predictor on half the configurations, predict the rest | The checked-step predictor does not beat the Kim-style baseline (task structure plus stock score) |
| E8 Perception | Owner forecasts each effect before the run and estimates it after | None. Report the gap between belief and measurement |
| E9 Overruled loop | A worker improves one output over 10 rounds with a visible score. Arms: no other check; a hidden check that never changes and reports pass or fail every round; a hidden check that is replaced every round. All arms are graded at the end by a check none of them met | The fixed hidden check ends as close to the final grade as the replaced one: the challenger adds nothing to the checked step. Or the visible-score arm does not drift from the final grade: the failure claim is wrong at this length |

Not run: single agent against many agents. Kim et al. tested it at a scale this project cannot match. Use their result and label each task's structure.

Outcome rule: the null stands if E7 fails. A deeper unit is supported if E7 passes and E2 survives. Decay is supported if E5 hits its kill condition. The overruled loop replaces the checked step as the alternative if E9 survives. Report split results as split.

---

# 6. Bracket: how any change gets in

Every proposed change, whether to Pro Stock, to a prompt or to this file, is a challenger against the current champion. One change per challenger. Each match is an A/B test: same tasks, same model, same budget, one difference.

| Round | Model and tasks | Runs | What it may decide |
|---|---|---|---|
| 1 Screen | Cheapest model, easiest tasks that are not at ceiling | 2 per arm | Eliminate only. Nothing is crowned |
| 2 Semi-final | Cheapest model, twice the tasks | 4 per arm | Halve the field again |
| 3 Final | Target model, sample size from the power analysis | As computed | Crown. Only the last two enter |

- Calibrate before every match. A match on tasks the champion passes more than 80% of the time decides nothing except cost.
- A challenger that loses a round is out.
- On a tie the champion keeps its seat, unless the challenger is cheaper. Then the challenger advances.
- Winners of single changes are combined. The combination must beat the best single winner before it can advance.
- Log every match in `BRACKET.md`: arms, tasks, runs, scores, cost, decision.

A/B testing is the match. The bracket is the schedule that keeps most matches cheap.

---

# 7. Method

- **Cheapest first.** Start every test on the cheapest model and the smallest tasks. Move up only for survivors of the bracket.
- **Power first.** From a 50% baseline, detecting a 15-point effect needs about 170 runs per arm; 20 points needs about 93. Version 1 planned 36 per arm, which detects only about 33 points. Estimate variance from calibration runs, then state the sample size and the smallest effect it can detect before running anything else.
- **Budget stop.** Before any batch above 200 runs, write the projected cost in the report and stop for the owner.
- **Paired and randomised.** The same tasks in every arm, order randomised, differences analysed per task, errors clustered by task.
- **Cost-controlled.** Report success against cost for every arm, never success alone.
- **Tasks.** Prefer published sets with deterministic verifiers (SkillsBench, Harness-Bench, ImpossibleBench for the probes). Hand-build only tasks from the owner's domains: documents, spreadsheets, support tickets. Keep tasks that stock passes 20 to 80% of the time.
- **Grading.** Scripts only for pass and fail. Held-out checks live outside the working folder. Failed transcripts are coded with MAST.
- **Tools.** Give each test arm only the tools its task needs. In the first screen a test agent created a scheduled task by accident.
- **Disclosure.** Record model, Claude Code version, flags and settings with every result.
- **Pre-registration.** Hash this file's sections 2 and 5 and the graders before the first run. Add no metric afterwards.
- **Traces.** Keep every transcript, score and cost on disk, raw.
- **Known obstacle.** A nested `claude -p` failed to authenticate in the cloud session where this was prepared. If it fails, use fresh-context subagents as arms and say so.

---

# 8. Reduction rules

If two concepts explain the same thing, keep one. If one can be derived from another, remove it. If a published study already settles a point at scale, cite it and do not rerun it. A concept that predicts nothing on held-out configurations is removed, however well it explains.

---

# 9. Phase 1 for Claude Code

1. Write the strongest case for the null and for decay, in two files, before anything else.
2. Build the smallest task set that is not at ceiling on the cheapest model, and calibrate it.
3. Run round 1 of the bracket for E0 and E3 on the cheapest model. Record E8 alongside.
4. Run the power analysis for the survivors. Report the sample size and the projected cost, then stop.
5. Report on one page: the decision first, then success against cost per arm, cheating rate, and what was not verified.

Do not install tools, change the owner's settings, or build Pro Stock.

---

# 10. Success condition

The project succeeds when one of these is shown with held-out prediction, not explanation:

1. The layers plus task structure and model strength predict best: the null stands.
2. The checked step predicts better: a deeper unit exists.
3. Effects vanish with model strength or tool updates: decay wins, and Pro Stock should stay minimal.
4. Results split, and the report says where.

Only confirmation bias is unacceptable.

---

# 11. Sources

See `EVIDENCE.md`.
