# 🧠 XKO Layer Mapping

This directory contains the **layer alias mapping** used throughout the XpectraNet SDK
to align symbolic cognition (L0–L9) with the simplified operational model (L0–L6).

---

## 📘 `layer_alias_map.json`

A JSON file mapping symbolic memory layers (`L0` to `L9`) to simplified aliases (`L0` to `L6`):

```json
{
  "L0": {"alias": "L0", "name": "Perception"},
  "L1": {"alias": "L1", "name": "Origin Insight"},
  "L2": {"alias": "L2", "name": "Remix"},
  "L3": {"alias": "L2", "name": "Remix"},
  "L4": {"alias": "L3", "name": "Synthesis"},
  "L5": {"alias": "L3", "name": "Synthesis"},
  "L6": {"alias": "L4", "name": "Validation"},
  "L7": {"alias": "L5", "name": "Canon"},
  "L8": {"alias": "L6", "name": "Archive"},
  "L9": {"alias": "L6", "name": "Archive/Myth"}
}
```

---

## 🔄 Why Alias the Layers?

To simplify real-world development while preserving symbolic richness:

- 🔁 L3 (Divergence) and L4 (Synthesis) → merged into `Remix` and `Synthesis`
- ✅ Canonical transitions (L1 → L2 → L3 → L4 → L5 → L6) supported in CirclePolicy
- 🧭 Reduces cognitive friction for validators, agents, and developers

---

## 🧩 Used In:

- `TrailManager` — to build remix trails using layer shifts
- `ValidatorEngine` — to check allowed transitions
- `CirclePolicy` — to enforce governance rules
- Insight display UIs — to group phases into cognitive bands

---

## 🛠 Tip for Contributors

If you add or refactor layers in `XKO`, update this alias map to keep agents and governance aligned.

