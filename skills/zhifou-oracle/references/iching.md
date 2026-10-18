# Three-coin I Ching

## Cast convention

Each coin contributes either 2 (yin) or 3 (yang). Three independent fair coins produce a line total: 6 old yin, 7 young yang, 8 young yin, 9 old yang. Values 6 and 9 move. The first cast is the bottom line; the sixth is the top. A record of six uniformly sampled totals is **not** a traditional three-coin cast: the correct line probabilities are 1/8, 3/8, 3/8, 1/8. A yarrow-stalk method has a different distribution and is not implemented here.

```sh
python3 scripts/oracle.py coin --lines 7,8,7,8,7,8
python3 scripts/oracle.py coin --coins '[[3,2,2],[3,3,2],[3,2,2],[2,3,3],[2,2,3],[3,3,2]]'
```

For a new cast, omit both import options. For a physical cast, establish which face maps to 2 and 3 before recording it; do not infer historical coin-face conventions from an unknown coin design. Imported totals do not imply invented individual coin faces.

## Declared changing-line convention

The tool follows the Zhu Xi-style framework already used in Zhifou. It is one later interpretive convention, not a uniquely prescribed algorithm in the primary Zhou Yi text.

| Moving lines | Selected reading |
| --- | --- |
| 0 | Primary judgment |
| 1 | That primary moving line |
| 2 | Both primary moving lines; upper is primary |
| 3 | Both judgments; primary as the main context and transformed as the change |
| 4 | Two unchanged lines of the transformed hexagram; lower is primary |
| 5 | The one unchanged line of the transformed hexagram |
| 6 | Qian uses Use Nine; Kun uses Use Six; otherwise transformed judgment |

Source framework: Zhu Xi, *Yi Xue Qi Meng*, *Kao Bian Zhan*. Do not present this selection policy as a complete account of every detail in Zhu Xi's practice, or silently substitute a different school's method. If the user requests another tradition, identify the difference and distinguish any manually selected passages from the tool's declared policy.

## Reading the result

`primary` and `transformed` include the original judgment, six line texts, Tuan, and Xiang. `selected_passages` identifies the actual passages and primary/supporting roles. Quote short excerpts with the hexagram number and line position. A passage can contain archaic or ominous imagery; explain its historical or symbolic context without predicting literal harm.

The tool returns a checksum and can verify a saved JSON result. This detects inconsistencies, not dishonest physical casts or tampering by someone who recomputes the checksum. It cannot prove supernatural validity, physical coin fairness, or the truth of an interpretation.
