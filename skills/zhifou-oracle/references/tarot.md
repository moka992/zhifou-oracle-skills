# Rider-Waite-Smith tarot

The local pack contains 22 major cards, four suits of 14 minor cards, 78 original-deck card fronts, and a card back. English names, Chinese names, imagery descriptions, and upright/reversed Chinese summaries are indexed by stable card ID. Strength is VIII and Justice is XI in this deck. Do not substitute Marseille numbering.

Waite's *The Pictorial Key to the Tarot* (1910) provides the historical reference. The bundled Chinese meanings are original **modern summaries**, not literal Waite quotations, a complete translation, or a claim that all modern tarot readers agree. Ask the model to paraphrase in the user's language; only quote historical English text after retrieving it from a verified source.

## Spreads

- `celtic-cross`: ten drawn positions, no separately chosen significator. This is an explicitly labelled adaptation of Waite's Celtic method, not an exact reconstruction of all his historical instructions.
- `three-card`: situation, challenge, next step. This is a modern reflection layout, not a specific claim about Waite's method.
- `single`: one focus card.

The Celtic Cross positions are present, crossing influence, crown, foundation, recent past, near future, self, environment, hopes/fears, and outlook. Orientations are fixed at draw time; the sideways placement of the crossing card is not itself a reversed orientation. A reversal is not a moral judgment or a guarantee of misfortune.

```sh
python3 scripts/oracle.py tarot --spread three-card
python3 scripts/oracle.py tarot --spread single --cards '[{"card_id":"major_08","reversed":false}]'
python3 scripts/oracle.py lookup --card cups_02
```

Each draw samples unique cards without replacement, with independent 50:50 orientation assignment. These are implementation choices, not proof of physical randomness or a predictive claim. Imported spreads preserve the user's exact orientations and order. Prefer synthesis of relevant positions to ten disconnected dictionary entries.

`card.image` is relative to this skill directory. A host with image tools may open or display those local JPEGs. A text-only host should use the supplied image description without claiming to have viewed the image. Death, the Devil, and the Tower are symbolic images, not literal death sentences, diagnoses, or evidence of a curse.
