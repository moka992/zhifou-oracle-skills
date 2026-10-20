# Distribution Plan

This is a venue review dated **2026-10-20**, not evidence that a listing or post has been submitted. Confirm current rules again at submission time. Account use, forks and external pull requests require the owner's explicit approval for the destination.

## Ready Now

The repository has a real [no-key demo](../tools/demo.py), a [complete reproducible case](walkthrough.md), the standard skill layout, a standalone release, source notices and a privacy-aware issue form. Lead with the runnable example rather than a claim that an agent can predict events.

The tools need Python 3.10+ and the standard library. Their output is structured data; model-written interpretation requires a host agent and may involve a subscription or API cost. English card names and documentation are available, but the bundled modern meaning summaries are primarily Chinese.

## Vetted Destinations

| Destination | Current requirement | Decision |
| --- | --- | --- |
| [heilcheng/awesome-agent-skills](https://github.com/heilcheng/awesome-agent-skills/blob/main/CONTRIBUTING.md) | Public skill, standard structure, documented usage and contribution review | A candidate after checking the matching section, duplicate entries and current contribution rules. Approval is not guaranteed. Prepare a focused entry, not a mass submission. |
| [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills/blob/main/CONTRIBUTING.md) | Explicitly requires demonstrated community usage and does not accept brand-new skills | **Defer.** Do not invent users, stars or adoption to satisfy the rule. Revisit after genuine integration examples exist. |
| [Show HN](https://news.ycombinator.com/showhn.html) | A substantive runnable project that the maker can discuss; easy trial; no vote solicitation | Potentially suitable for the no-key local tools, subject to [current account restrictions](https://news.ycombinator.com/showlim). The account owner should publish and answer questions. |
| [V2EX](https://v2ex.com/about) | Prohibits AI-generated posts | Do not paste generated launch copy. The maker can independently decide whether to write a firsthand account in their own words. |

## Candidate Directory Entry

Use only if the destination accepts the topic and entry format:

```markdown
- **[moka992/zhifou-oracle](https://github.com/moka992/zhifou-oracle-skills/tree/main/skills/zhifou-oracle)** - Offline I Ching and tarot with fixed, source-backed outcomes.
```

Suggested PR title: `Add skill: moka992/zhifou-oracle`.

Suggested explanation:

> This portable Agent Skill separates local draws and source retrieval from model interpretation. It includes a reproducible no-key demo, imported-result verification, documented method variants and separately attributed datasets/artwork. It is intended for cultural study and symbolic reflection, not predictive claims. The original tools/instructions are MIT; the Zhou Yi corpus remains CC BY-SA 4.0.

This is a draft, not a submitted PR, accepted listing, vendor endorsement or host certification.

## Show HN Draft

Title: **Show HN: I Ching and tarot tools that keep agent-generated readings grounded**

The local tools draw or import a result, retrieve the relevant material, and return a verifiable record. The model interprets that record instead of quietly choosing different cards or inventing a cast. A fixed-input demonstration runs with Python's standard library, without an API key or service account.

The package includes 64 hexagrams, 384 line texts, 78 historical Rider-Waite-Smith cards, documented method choices, and source notices. The tests exercise all 4,096 six-line value combinations. That checks software consistency, not whether divination predicts events. There is also an example interpretation explicitly labelled as editorial rather than a model benchmark.

Try it: https://github.com/moka992/zhifou-oracle-skills#try-it-in-a-minute

For the maker to add before posting: explain the actual motivation and experience in their own words, disclose relevant assistance, and be available to discuss tradeoffs. Do not invent a personal story, usage count or model-quality result.

## Follow-Up

Collect one concrete integration report or failure example at a time. Review actual visits, downloads and issues after a real distribution event. Clone counts are not user counts. Do not promise a star target or turn the project into repeated unsolicited link drops.
