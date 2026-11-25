# The strongest case for the null

Claim: the layers (harness, loop, graph) are the right units. Task structure and model capability decide whether a layer helps. A "checked step" adds vocabulary, not prediction.

## 1. It already predicts, out of sample, at scale

Kim et al., *Towards a Science of Scaling Agent Systems* (arXiv:2512.08296, Google Research, DeepMind, MIT; v3 April 2026) ran 180 configurations: five architectures, three model families, four benchmarks. A predictor built from task structure and model capability picks the best architecture for 87% of held-out configurations and validated on an unseen frontier model (MAE 0.071). Multi-agent coordination gained +81% on a parallel finance task and lost 70% on a sequential planning task. No version of the checked-step idea has a held-out number at all. The burden of proof sits with the challenger.

## 2. The checked step is a re-description of results the null already explains

- Checks help: a verifier is a loop layer. Kim's centralised architectures cut error amplification from 17.2x to 4.4x by adding an orchestrator that checks sub-agents. That is "a check outside the worker", and it was predicted by architecture plus structure.
- Context hurts: Gloaguen et al. (arXiv:2602.11988, ETH Zurich, ICLR 2026) found repository context files do not raise success and raise cost by over 20%; LLM-written files hurt, developer-written ones help slightly. That is a property of the context layer and its author, measurable without a new unit.
- Skills help when curated: SkillsBench (arXiv:2602.12670) found curated skills +16 points on average, self-written ones about −1, with focused skills beating long ones. Again: a layer property (who wrote it, how long), not a feedback count.

Any finding phrased as "external feedback per step" can be rephrased as "this layer, on this task structure, with this model". If both phrasings predict the same thing, section 8 of the README says keep one, and the null came first.

## 3. "Feedback per step" is hard to measure before the run

The null's predictors (parallel or sequential, stock score, model tier) are labelled before any run, cheaply. "Trustworthy external feedback per step" depends on whether the check is gamed, whether the reference is right, and how often it runs, which are known only after the run. A predictor that needs the outcome to measure its input does not predict.

## 4. What would make the null lose

E7: the checked-step predictor beats task structure plus stock score on held-out configurations. Short of that, the null stands by the README's own outcome rule.

## 5. The weak point, stated honestly

Kim's 180 configurations vary architecture, not standing context, state files or check types. The null's 87% is about "how many agents and how connected", one of the five layers in the research question. For E0 (state across sessions) and E3 (standing text) the null has only a weaker form: "the stock score and task structure explain most of the variance; the treatment adds noise". That is what this phase tests.
