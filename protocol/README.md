# 💠 protocol/staking.py — XPDT Staking Logic

This module implements symbolic XPDT staking logic for validation, canonization, and memory governance in the XpectraNet Protocol.

---

## ✅ What It Does

- Verifies if an agent has enough XPDT to participate in:
  - Validation (L6)
  - Canonization (L7)
  - Memory-based scoring or ritual enforcement
- Calculates symbolic reward distributions after Circle votes

---

## 🔍 Methods

```python
from protocol.staking import XPDTStaking

XPDTStaking.meets_stake_requirement(agent, min_required)
XPDTStaking.distribute_reward(total_xpdt, validators, split)
```

---

## 🧬 Agent Stake in CirclePolicy

Your `circle-policy.yaml` can include:

```yaml
quorum:
  requiredStake: 1.0
  validatorSplit: [0.4, 0.4, 0.2]
```

Then use:

```python
from validation.validator import ValidatorEngine
from protocol.staking import XPDTStaking

if XPDTStaking.meets_stake_requirement(agent, policy.rules["quorum"]["requiredStake"]):
    ValidatorEngine.validate_insight(...)
```

---

## 📦 Distribution Example

```python
XPDTStaking.distribute_reward(
    total=10.0,
    validators=[{"glyph": "A"}, {"glyph": "B"}, {"glyph": "C"}],
    split=[0.4, 0.4, 0.2]
)
```

Results in:

```json
[
  { "recipient": "A", "amount": 4.0 },
  { "recipient": "B", "amount": 4.0 },
  { "recipient": "C", "amount": 2.0 }
]
```

---

## 🧠 Future Ideas

- Staking history tracking  
- Slashing / penalty rules for invalid votes  
- Integration with XPDT token ledger for proof of stake

