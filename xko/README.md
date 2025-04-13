# 🧠 xko/ — Xpectra Knowledge Ontology (Layers L0–L9)

This folder defines the core symbolic structure of the XpectraNet Protocol — how insights evolve through cognitive layers of meaning.

---

## 🔢 What Are XKO Layers?

Each insight in XpectraNet exists in one of 10 cognitive layers, from raw perception (L0) to universal symbolic archetypes (L9).

They help agents:
- Track memory evolution
- Assign meaning across contexts
- Guide remix, validation, and canonization decisions

---

## 📘 Files

| File               | Description                                           |
|--------------------|-------------------------------------------------------|
| `layer_map.py`      | Python map of layers and roles                       |
| `layer_map.jsonld`  | Semantic JSON-LD ontology for XKO layers             |

---

## 🧬 Sample Layer

```json
{
  "@id": "xko:L5",
  "name": "Emotional Logic",
  "description": "Memory weighted by emotional contradiction or resonance.",
  "symbolicRole": "feel + guide",
  "cognitiveBasis": "valence alignment / narrative tension"
}
```

---

## 🧭 Use This For:

- Memory graphs
- Semantic UI overlays (color by layer)
- Insight validation logic
- Wikidata/LD interoperability

---

## 🔗 Publish or Extend

To serve your JSON-LD publicly:

1. Host `layer_map.jsonld` at: `https://xpectranet.org/xko/layer_map.jsonld`
2. Register namespace: `https://xpectranet.org/xko#`
3. Add more vocab (e.g. `xko:Agent`, `xko:RemixIntent`, `xko:TrailNode`)

