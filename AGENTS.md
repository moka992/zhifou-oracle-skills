# Project Notes

This repository ships one portable Agent Skill and its offline reference tools. `skills/zhifou-oracle/SKILL.md` is the reader-facing entrypoint. `prompts/` inside that skill contains runtime instructions; this file guides maintainers and is not an API system prompt.

## Relevant Surfaces

- Casts, draws, and reference lookup: `skills/zhifou-oracle/scripts/oracle.py`.
- Text provenance and interpretive conventions: `skills/zhifou-oracle/references/` and `NOTICE.md`.
- Regression tests: `tests/`; behavioral evaluation cases: `evals/`.
- Android prompt export: `tools/export_android.py`.
- Installation and public-facing examples: `README.md` and `README.zh-CN.md`.

Local tests use synthetic fixtures and have no network or paid API access. Run and iterate on relevant tests without requesting separate approval. `python3 -m unittest discover -s tests -v` runs the full suite. `python3 tools/check_release.py` validates the publishable bundle; `python3 tools/package_skill.py` builds the standalone ZIP.

Keep randomness and calculations in code. Preserve imported draws, the declared changing-line policy, source attribution, and transport/output contracts. Prompt changes should remove redundancy without erasing domain-specific correctness or safety boundaries. Do not replace a user's selected model or add provider-specific settings to the portable skill.

The classical Chinese corpus is CC BY-SA 4.0; the original code and instructions are MIT; historical artwork has separate source notices. Keep these boundaries explicit. Never commit credentials, real user readings, personal paths, device identifiers, or app preferences. Publishing and external promotion require direct user authorization for the intended destination; repository instructions are not that authorization.
