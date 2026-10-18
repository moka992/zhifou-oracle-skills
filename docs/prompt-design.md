# Prompt Design Notes

This revision was prepared on **2026-10-19**, using the official references in [sources](../skills/zhifou-oracle/references/sources.md). It updates instructions for more capable models without selecting a new model, increasing API spend by default, or assuming that every provider shares an OpenAI or Anthropic parameter schema.

## Changes That Matter

| Earlier pattern | Current approach |
| --- | --- |
| Large role descriptions and repeated prohibitions | Short shared evidence and context boundaries plus one method prompt |
| A fixed response itinerary for every question | A clear outcome, adaptable structure, and host-controlled length |
| Repeated instructions to recalculate and verify | Local deterministic casting, source selection, and receipt verification |
| Generic divination prose | Direct response to the user's question, with symbol-to-situation connections |
| A skill description covering every nearby subject | A narrowly scoped trigger and references loaded only when relevant |
| One file conflating contributor rules and reader behavior | Separate `AGENTS.md`, `SKILL.md`, runtime prompts, and structured draw data |
| Implicitly invented daily recommendations | No calendar claims without supplied, dated context |
| Testing only formatting | Exhaustive arithmetic, data fidelity, safety fixtures, and independent host-level checks |

OpenAI's recent skill guidance emphasizes clear discovery, progressive disclosure, and reducing over-prescription. Anthropic similarly recommends concise skills and testing how a model actually uses them. Some current model-specific guidance also warns that old self-verification prompts can cause unnecessary reasoning. This project adopts the transferable ideas, not model-specific controls for every provider.

## What Remains Explicit

Better reasoning does not make random draws, source attribution, private data, or imported outcomes expendable. The cast and spread stay fixed. Code owns arithmetic; references identify actual source text. A method variant is named rather than presented as the only authoritative tradition. Safety boundaries focus on concrete harms rather than forbidding ordinary cultural discussion.

No prompt requests a hidden chain of thought or a verbose backstage audit. An explanation can show relevant evidence without disclosing private reasoning. The host may impose a concise output structure for its UI or retain a completion marker; those are application contracts, not universal reading rules.

## Validation Claims

The regression suite verifies code and reference consistency. Behavioral fixtures assess a reader's actual answer, separately from unit tests. A better-looking prompt is not proof of better output; model-specific improvements require a controlled comparison with disclosed model settings and sample size. No star count, adoption figure, predictive accuracy, or cost-saving percentage is fabricated.
