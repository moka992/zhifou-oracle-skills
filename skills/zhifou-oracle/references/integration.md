# Host and API integration

## Three different instruction layers

`AGENTS.md` and `CLAUDE.md` guide agents maintaining this repository. `SKILL.md` is the portable workflow entrypoint. `prompts/*.md` are concise runtime instructions for a host to load into its system/developer instruction surface. A model reached by API does not automatically discover any of these files.

For an application, load `prompts/core.md` and the relevant method prompt into a trusted instruction message. Put the user's question and the generated reading record into a separate, structured user-data message, preferably JSON. Treat retrieved text and profile values as data, not as extra system instructions. Never interpolate user text into a shell command.

The standalone tools produce source-backed JSON and never call a model. Your host owns provider authentication, actual model selection, context limits, output budgets, transport, streaming, and storage. A host's existing model should not be silently replaced with a flagship. A longer reasoning budget is not automatically a better user experience.

The common prefix is stable and small; append only the chosen method's instructions and the specific draw. Do not insert the entire 64-hexagram or 78-card catalog into every request. Matching prefixes can help provider caching, but a cache hit or a cost reduction is not guaranteed across providers or account configurations.

The Android exporter in `tools/export_android.py` creates Kotlin constants from these exact prompt files. It does not modify endpoints, credentials, reasoning settings, token limits, caching, or completion-marker handling. This repository's package remains usable without Android.

## Outputs and receipts

Receipts contain a version, method, origin, the outcome, and a SHA-256 of a canonical outcome payload. Question and optional context are intentionally outside that checksum. `verify` checks both the checksum and derived metadata against bundled references. It is a consistency check, not a signature, proof of a physical draw, or proof that a reading is true.

For private questions, use `--question-stdin`. Scripts do not log, persist, or transmit input, but stdout, shell redirection, host conversations, and host model providers can retain it. Do not commit real output records. An optional `--context` JSON accepts a small set of dated calendar and focus fields; unknown fields are rejected. Almanac entries use an exact safe allowlist. The skill does not calculate lunar dates or verify caller-provided weather, calendars, or profiles.

## Compatibility and evaluation

The layout follows the common Agent Skills structure and includes optional Codex UI metadata. Install in a host's skill directory; do not assume all frontmatter extensions or all image/tool features are supported by every host. Tested local behavior is reported separately from model behavior in `evals/README.md`.

Use the behavioral cases when changing prompts or models. Check fidelity to the draw, question relevance, source accuracy, privacy, and proportionate uncertainty. Local unit tests cannot demonstrate that a remote model will comply. Provider-specific APIs and model migrations should use that provider's current official documentation rather than a universal parameter recipe.
