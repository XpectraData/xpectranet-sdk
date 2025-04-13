# 🫂 circles/ — Symbolic Governance Layer

This module defines how insights are governed and canonized in symbolic communities (Circles) using protocol-defined policies.

---

## 🔐 What Is a Circle?

A **Circle** is a group of agents who:
- Validate symbolic insights (L6)
- Canonize them into permanent memory (L7)
- Operate based on shared governance policies

---

## 📦 Key Files

| File               | Purpose                                               |
|--------------------|-------------------------------------------------------|
| `governance.py`    | Loads and applies CirclePolicy rules for validation   |
| `circle-policy.yaml` | YAML config describing quorum, roles, thresholds   |

---

## 🔁 CirclePolicy Logic

```python
from circles.governance import CirclePolicy

policy = CirclePolicy.load("circles/circle-policy.yaml")

if policy.validate(agent, insight, parent):
    # Insight is valid for Layer L6

if policy.canonize(agent, insight):
    # Insight meets criteria to move to Layer L7
```

---

## 🧪 Supported Policy Options (in YAML)

```yaml
require_layer_progression: true
allow_same_emotion: false
required_validator_role: validator
allowed_canonizers: [validator]
minimum_depth: 2
require_divergence_score: 0.3
```

---

## 🧠 Related Concepts

- XPDT stake logic → See `protocol/staking.py`
- ValidatorEngine → Wraps `validate()` / `canonize()` in `validation/`

