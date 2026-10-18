<p align="center"><img src="docs/assets/cover.png" alt="知否占卜技能：本地抽取，有据解读" width="100%"></p>

# 知否占卜 Agent Skill

**让模型解读真实的抽取结果，而不是临场编造一个结果。**

[English](README.md) · [下载 Skill](https://github.com/moka992/zhifou-oracle-skills/releases/latest) · [方法与出处](skills/zhifou-oracle/references/sources.md) · [验证说明](evals/README.md)

一个可独立使用的 Agent Skill：铜钱卦、韦特塔罗、原创答案卡。本地程序负责抽取、计算和查找原文，模型负责理解问题与组织解读。工具只依赖 Python 标准库，不需要 API Key、服务器或额外 Python 包；宿主模型本身仍可能需要订阅或 API 费用。

项目从 Android 应用[知否运势](https://github.com/moka992/zhifou-fortune)的离线占卜模块整理而来，不包含应用用户数据、个人配置或模型文件。

## 包含什么

| 部分 | 内容 |
| --- | --- |
| 铜钱卦 | 三枚铜钱逐爻生成六爻，正确的 1:3:3:1 概率、初爻至上爻顺序、本卦、动爻、变卦与明确标注的变占规则 |
| 周易参考 | 64 卦、384 爻、卦辞、《彖》《象》与用九用六，保留原文出处和数据授权 |
| 韦特塔罗 | 完整 78 张历史牌面与牌背、中英文牌名、图像描述、原创现代中文正逆位概括 |
| 牌阵 | 单张、现代三张反思牌阵，以及不另设指示牌的十张十字牌阵 |
| 原创答案卡 | 100 条本项目原创短句及建议，不是商业《答案之书》的摘录 |
| 结果记录 | 导入结果不会被重抽；校验工具检查数值、经文取用、牌位与正逆位的一致性 |
| 可复用提示词 | 标准 `SKILL.md`、按需读取的参考资料、运行时提示词及 Codex 显示元数据 |

这是一套文化与象征解读工具，不声称占卜已经得到科学预测验证。昵称、生日、位置权限和文字问题都不是必要条件；心中默念也可以。

## 快速尝试

```sh
git clone https://github.com/moka992/zhifou-oracle-skills.git
cd zhifou-oracle-skills
python3 skills/zhifou-oracle/scripts/oracle.py coin
python3 skills/zhifou-oracle/scripts/oracle.py tarot --spread celtic-cross
python3 skills/zhifou-oracle/scripts/oracle.py answer
```

这些命令输出 JSON 结果与相关参考资料，不会自行调用模型。加载 Skill 后，Agent 再结合用户的问题进行解读。

## 安装

在克隆的仓库中执行，选择实际使用的宿主与目标项目：

```sh
python3 tools/install_skill.py --host codex --project /path/to/your-project
python3 tools/install_skill.py --host claude --project /path/to/your-project
```

分别安装到目标项目的 `.agents/skills/zhifou-oracle` 或 `.claude/skills/zhifou-oracle`。默认拒绝覆盖已有安装，通常只需选择其中一种。必要时按宿主要求刷新技能发现。

在 Codex 中：

```text
使用 $zhifou-oracle，为我做一次铜钱卦解读。
我的问题是：面对这次工作上的选择，我最应该看清什么？
请围绕问题、取用经文与现实条件来讲，不要重新抽取结果。
```

Claude Code 对应使用 `/zhifou-oracle`。也可下载 [Release ZIP](https://github.com/moka992/zhifou-oracle-skills/releases/latest)，按其他支持 Agent Skills 的宿主要求安装。图片查看、脚本执行及自动发现是否可用，仍取决于宿主。

## 导入已有结果

```sh
python3 skills/zhifou-oracle/scripts/oracle.py coin --lines 6,7,8,9,7,8
python3 skills/zhifou-oracle/scripts/oracle.py tarot --spread single --cards '[{"card_id":"major_08","reversed":true}]'
python3 skills/zhifou-oracle/scripts/oracle.py lookup --hexagram 1
python3 skills/zhifou-oracle/scripts/oracle.py lookup --card cups_02
```

铜钱卦数值按从下至上的顺序输入。只有用户提供总数时，不会编造三枚铜钱各自的正反面。塔罗导入必须明确牌位顺序与布尔值正逆位，不能重复同一张牌。

可用 `verify path/to/reading.json` 校验保存的结果。它检查内部一致性，不证明实体投掷的真实性、结果不可伪造或解读一定正确。校验和不包含用户提问。

私密问题建议通过 `--question-stdin` 输入，避免留在命令行历史中。脚本不保存或上传问题，但宿主对话、终端输出及模型平台仍可能保留内容。不要将真实占卜记录提交到仓库。

## 接入应用

`AGENTS.md` 是开发代理的仓库指引，不会自动成为 API 提示词。应用需要显式加载[运行时提示词](skills/zhifou-oracle/prompts)，再把提问和已确定的结果作为结构化数据传入。无需每次塞入整部经典或全部牌库。

项目提供 [Android Kotlin 导出工具](tools/export_android.py)，从同一份提示词生成常量。不改动已有平台、密钥、模型选择、推理参数或 token 上限。详见[集成说明](skills/zhifou-oracle/references/integration.md)和[提示词设计说明](docs/prompt-design.md)。

## 验证与边界

```sh
python3 -m unittest discover -s tests -v
python3 tools/check_release.py
python3 tools/package_skill.py
```

自动测试穷举全部 **4,096 种六爻数值组合**，并覆盖投掷概率、变占取用、牌库完整性、导入结果、正逆位保留、校验篡改、上下文过滤和私密输入。它们证明程序规则得到检查，不证明预测能力。

[行为评估用例](evals/cases.json)另行检查问题相关性、默念提问、敏感牌面、引文、提示词注入及高风险问题。模型表现需要独立验证；不把离线单元测试包装成模型能力测试，也不承诺未经测量的准确率或提升比例。

黄历仅接受调用方主动提供的有日期上下文，本 Skill 不计算农历黄历，不擅自联网获取天气或位置。塔罗的历史牌义、现代概括与个人建议分开处理，不把不同传统混成命定因果。

## 开源授权

原创代码、提示词、答案短句与现代概括使用 **MIT**；Kanseki《周易》适配数据继续使用 **CC BY-SA 4.0**，不是 MIT。1909 年原版韦特历史牌面保留独立来源说明，不包含现代商业牌组或商业译本。详见 [NOTICE](skills/zhifou-oracle/NOTICE.md)。

欢迎提供出处纠正、实际失败案例、翻译与集成示例。请先阅读[贡献说明](CONTRIBUTING.md)及[隐私安全说明](SECURITY.md)。觉得项目有用，可以用 Star 帮助更多人发现；有可复现的问题，也欢迎提交 Issue。
