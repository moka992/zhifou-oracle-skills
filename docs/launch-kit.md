# Launch Kit

These are ready-to-adapt announcements, not records of posts already made. Publish only in relevant venues that accept this type of project. Lead with a reproducible example; do not mass-post, purchase engagement, or imply vendor endorsement.

The current assets are a [no-key reproducible demo](../tools/demo.py), [complete English/Chinese case](walkthrough.md), and [rendered actual tool output](assets/offline-demo.svg). Read the [venue review and submission drafts](launch-channels.md) before choosing a destination. Some directories require existing adoption, and some communities prohibit AI-generated posts; those are not suitable places to paste generic launch copy.

## Short English Introduction

**Zhifou Oracle Skills: I Ching and tarot where the agent interprets the draw instead of inventing it.**

A portable Agent Skill with offline three-coin casting, 64 hexagrams and 384 line texts, the full historical 78-card Rider-Waite-Smith deck, and 100 original reflection prompts. Python standard library only for local tools. Imported outcomes stay fixed, sources are attributed, and the six-line calculations are exhaustively tested.

It's built for symbolic reflection and cultural study, not guaranteed predictions. The repo includes installation steps, reproducible examples, behavioral evaluation cases, and explicit dataset licenses.

https://github.com/moka992/zhifou-oracle-skills

## 中文介绍

**把知否运势的占卜基础整理成了一个独立 Agent Skill：模型负责解读，程序负责抽取和计算。**

包含铜钱卦、64 卦与 384 爻原文、完整 78 张历史韦特牌面、100 条原创答案短句。工具仅依赖 Python 标准库，保留导入结果与原文出处，并穷举检查全部 4,096 种六爻组合。

不是宣称 AI 能预知未来，而是希望文化与象征解读少一点凭空编造，多一点可核对的方法、材料与边界。支持按 Agent Skills 格式集成，仓库提供中英文文档、运行示例和行为评估用例。

https://github.com/moka992/zhifou-oracle-skills

## Suggested Demonstration

1. Import a specific cast or a reversed tarot card and show that the outcome remains fixed.
2. Ask a focused work or communication question.
3. Compare the actual cited source to the interpretation; distinguish a paraphrase from a quotation.
4. Show the privacy boundary and a meaningful limitation, not only a flattering answer.

The original AI-generated cover is `assets/cover.png`, with its generation note in [asset notes](assets/README.md). The three historical card previews in the README come from the separately attributed RWS pack.

## Asset and Tracking Checklist

- Use `docs/assets/social-preview.jpg` as a compact link-preview image; it is a resized version of the attributed cover, not an application screenshot.
- Regenerate `offline-demo.svg` with `python3 tools/render_demo.py`; do not hand-edit PASS lines or present the image as a hosted model result.
- Keep owner-only traffic snapshots private. [The app repository's metrics tool](https://github.com/moka992/zhifou-fortune/blob/main/tools/repository_metrics.py) can read this repository with `--repo moka992/zhifou-oracle-skills`.
- After an actual approved post, record its link privately and review real visits, downloads and actionable feedback. Do not count a prepared draft as a published announcement.
