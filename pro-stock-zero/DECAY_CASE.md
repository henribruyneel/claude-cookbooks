# The strongest case for decay

Claim: whatever a procedure adds is temporary. Gains shrink as models get stronger, and working practice moves into the default tool. The unit that matters is the model plus its default harness.

## 1. The record shows the gains are largest on the weakest setups

- SkillsBench (arXiv:2602.12670): smaller models with curated skills match larger models without them. A gain that lets a small model reach a large one is, by definition, a gain the large model already has.
- Gloaguen et al. (arXiv:2602.11988): context files do not raise success for current coding agents and raise cost by over 20%. Instructions that once compensated for weak instruction-following now mostly add exploration and cost.
- Kim et al. (arXiv:2512.08296): multi-agent benefit depends on model capability; capable single agents leave less for coordination to recover, and the same paper reports error amplification when coordination is added without need.

## 2. The tools absorb the practice

Each technique Pro Stock might add has already moved into Claude Code's default harness at some point: plan mode, to-do tracking, subagents, memory, compaction, permission classifiers, code review, skills. A procedure that duplicates a default pays the context cost twice and may conflict with the default's wording. The procedure ages each time the tool ships; the tool does not age relative to itself.

## 3. Cost is certain, benefit is conditional

Standing text is paid in every session; its benefit is paid only on the tasks where the model would otherwise have failed in the way the text prevents. As the base failure rate falls, the expected benefit falls with it and the cost does not. Below some failure rate every always-loaded line is a net loss. That rate is moving in one direction.

## 4. Predictions decay makes that the others do not

- E3: the 3-line arm ties or beats the full procedure on the cheapest model already, and the full procedure plus 20k irrelevant tokens loses.
- E5: whatever gain E1 or E2 shows on the weaker model shrinks on the stronger one.
- Over calendar time: re-running a crowned change after a model or tool update should show a smaller effect. (Not testable in phase 1.)

## 5. What would make decay lose

A treatment whose gain is equal or larger on the stronger model (E5), or a gain that cannot be absorbed into a tool because it depends on owner-specific information the tool cannot have (the owner's reference, the owner's domain). The second is the strongest objection: a check against the owner's own reference cannot be shipped in a default harness. Decay predicts the procedure should shrink to exactly that owner-specific remainder.
