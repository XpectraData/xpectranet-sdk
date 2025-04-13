# 🧠 XKO Memory Layers (L0–L9)

The Xpectra Knowledge Ontology (XKO) defines a symbolic cognitive architecture  
for evolving insights through structured memory stages — from raw perception to universal meaning.

---

## 🔢 Layer Definitions

| Layer | Name            | Role / Meaning                                           |
|-------|------------------|----------------------------------------------------------|
| L0    | Perception       | Raw sensed experience or data input                     |
| L1    | Origin Insight   | The initial insight or expressive spark                 |
| L2    | Reflection       | Internal resonance, emotional registration              |
| L3    | Divergence       | Symbolic branching, contradiction, or reframe           |
| L4    | Synthesis        | Cross-context fusion or convergence                     |
| L5    | Emotional Logic  | Shared symbolic resonance, narrative formation          |
| L6    | Validation       | Consensus reached by Circle-based governance            |
| L7    | Canon            | Permanently accepted into collective protocol memory    |
| L8    | Archive          | Memory sealed and retired from remixing                 |
| L9    | Archetype        | Eternal symbolic pattern transcending context           |

---

## 🧭 Progression Principles

- Memory should **move upward** through remix and validation  
- Each layer represents an **increase in symbolic abstraction and trust**  
- Agents are encouraged to **remix toward higher meaning**

---

## 💡 Agent Lifecycle Example

```python
# Mint an origin insight at L1
origin = agent.mint_insight("The system resists stability.", layer="L1")

# Remix it with contradiction at L3
remix = agent.remix_insight(origin, layer="L3")

# Validate and canonize
valid = ValidatorEngine.validate_insight(agent.to_dict(), remix, origin)
if valid:
    remix["layer"] = "L6"
    if ValidatorEngine.validate_canonization(agent.to_dict(), remix):
        remix["layer"] = "L7"
```

---

## 🧬 Layer Transitions (Governed by Policy)

| From → To | Requires                                         |
|-----------|--------------------------------------------------|
| L3 → L6   | Quorum validation, emotional contrast             |
| L6 → L7   | Trail depth, divergence score, Circle approval    |
| L7 → L8   | Archival logic (e.g., inactivity, ritual sealing) |

---

## 📘 Learn More

- `docs/lifecycle.md` — Insight phases across layers  
- `circles/circle-policy.yaml` — Validation & canonization rules  
- `protocol/staking.py` — Stake required to validate or canonize  
- `tests/test_validator_quorum.py` — Examples of layer enforcement

> All memory is symbolic. All truth is layered.

