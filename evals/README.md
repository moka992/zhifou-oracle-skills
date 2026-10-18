# Behavioral Evaluation

`cases.json` contains synthetic requests and observable grading criteria. These are evaluation fixtures, **not** user conversations or few-shot examples automatically inserted into every reading.

Run the local unit suite for deterministic calculations, imports, integrity, privacy, and packaging. That suite does not call an LLM and cannot establish prompt adherence, model quality, predictive validity, or a cross-model improvement percentage.

For a model or prompt change:

1. Load the skill in the target host, or load its core/method prompts through the host's API instruction surface.
2. Materialize each supplied cast or card list with the local tool. For a lookup case, retrieve the requested reference without drawing.
3. Present the synthetic request and that exact record. Grade the case's listed checks and source fidelity. Record model/version, host, prompt revision, settings, date, and any failures.
4. Compare against the previous prompt on the same fixtures. Report the sample size and limitations, including the model's stochastic behavior.

Live API evaluation is intentionally not automatic. It requires a user-authorized provider account, may cost money, and must not use real private readings as fixtures. A reviewer may carry out a limited host-agent forward test, but that is not a benchmark of every supported API model.

## Current Validation

Local deterministic regressions are executed by CI. Any independent host-agent evaluation is documented in `REPORT.md` when performed. Absence of a model report means the model-specific behavioral claims have not been measured, not that the skill passed every case.
