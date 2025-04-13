# 🔄 Circle Governance

Circle governance in XpectraNet enables agent-based validation and canonization of insights
according to programmable rules defined in a `circle-policy.yaml` file.

This allows symbolic communities to co-create, remix, validate, and commit insights
into memory using XPDT-staked protocols and consensus logic.

---

## ⚖️ What a Circle Policy Defines

- ✅ Which layer transitions are allowed
- 🧠 Which agents (by role and glyph) can validate, remix, or canonize
- 🔁 How Circle validation interacts with XPDT and quorum
- 🔗 Transition enforcement via **layer alias mapping**

---

## 🧠 Layer Aliasing (L0–L9 → L0–L6)

Circle governance uses **operational layer aliases** so policies remain easy to write, even with full symbolic depth.

| Symbolic Layer | Alias | Layer Role           |
|----------------|--------|-----------------------|
| L0             | L0     | Perception            |
| L1             | L1     | Origin Insight        |
| L2             | L2     | Remix                 |
| L3             | L2     | Remix (Divergence)    |
| L4             | L3     | Synthesis             |
| L5             | L3     | Emotional Synthesis   |
| L6             | L4     | Validation            |
| L7             | L5     | Canon                 |
| L8             | L6     | Archive               |
| L9             | L6     | Archive/Myth          |

---

## 📘 Example Policy: `circle-policy.yaml`

```yaml
minStake: 1.0

allowedTransitions:
  - from: L1
    to: L2
  - from: L2
    to: L3
  - from: L3
    to: L4
  - from: L4
    to: L5
  - from: L5
    to: L6

layerAliases:
  L0: Perception
  L1: Origin Insight
  L2: Remix
  L3: Synthesis
  L4: Validation
  L5: Canon
  L6: Archive/Myth

validators:
  - role: "circle-member"
    glyph: "ψ-Echo"
    permissions:
      - canValidate: true
      - canCanonize: true
      - canRemix: true
```

---

## ✅ Managed by `governance.py`

The SDK loads and validates Circle policy via:

- `CirclePolicy.load(path)`  
- `.is_transition_allowed(from, to)`  
- `.can_validate(agent)`, `.can_canonize(agent)`, `.can_remix(agent)`

Used directly inside:
- `ValidatorEngine`  
- `QuorumEngine`  
- `Agent remixer + validator logic`

---

For full alias structure: [`layer_alias_map.json`](https://github.com/XpectraData/xpectranet-sdk/blob/main/xko/layer_alias_map.json)
