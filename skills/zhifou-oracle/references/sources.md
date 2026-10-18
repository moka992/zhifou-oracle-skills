# Sources and attribution

## Domain sources

- Zhou Yi received Chinese text: [Kanseki Repository KR1a0001](https://github.com/kanripo/KR1a0001), revision `8284adbf9e3435d713180e24f05bf75f8b7d1d96`. Adapted dataset: **CC BY-SA 4.0**, including extraction, removal of page markers, and structured JSON conversion. See [NOTICE.md](../NOTICE.md).
- Changing-line convention: Zhu Xi, *Yi Xue Qi Meng*, *Kao Bian Zhan*. This names the traditional framework; the exact implemented selection table is documented in [I Ching method](iching.md). It is not the only interpretive school or a claim to reproduce every detail of a historical edition.
- Tarot artwork: Pamela Colman Smith, Rider, 1909, original [Roses & Lilies collection](https://commons.wikimedia.org/wiki/Category:Rider-Waite_tarot_deck_(Roses_%26_Lilies)). Historical card fronts and back, with source notes in `assets/RIDER_WAITE_SMITH.txt`.
- Tarot historical text: A. E. Waite, [The Pictorial Key to the Tarot](https://en.wikisource.org/wiki/The_Pictorial_Key_to_the_Tarot), especially [Part III](https://en.wikisource.org/wiki/The_Pictorial_Key_to_the_Tarot/Part_3). Bundled modern Chinese summaries are not a verbatim translation.
- Dao De Jing: [Chinese Text Project](https://ctext.org/dao-de-jing/zh). Consult a verified passage before quoting it; this pack does not bundle a complete Dao De Jing corpus.
- The 100 reflection entries are original Zhifou content, not copied from a commercial answer book.

## Prompt and skill design references

Checked **2026-10-19**. These sources inform engineering choices, not divination claims or vendor endorsement.

- OpenAI, [Rethinking skills and prompts for GPT-6 Astra](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra): concise discovery descriptions, progressive disclosure, and task-specific boundaries instead of over-prescribed itineraries.
- OpenAI, [Skills](https://developers.openai.com/codex/skills), and [AGENTS.md](https://developers.openai.com/codex/guides/agents-md): separate reusable workflows from repository guidance.
- Anthropic, [Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices): task-relevant references, deterministic scripts, and behavioral evaluation.
- Anthropic, [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices): clear outcomes, context/data boundaries, and removal of prompting that causes redundant verification.
- Anthropic, [Claude Code skills](https://code.claude.com/docs/en/skills): discovery, installation, supporting files, and invocation.

This is an independent community project. OpenAI, Anthropic, Kanseki Repository, and Wikimedia do not endorse it. Model-agnostic instructions do not imply a measured quality improvement on every model.
