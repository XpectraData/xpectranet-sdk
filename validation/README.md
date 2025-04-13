# `validation/` — Governance Validation Engine

This module defines how symbolic insights are evaluated against Circle rules for validation and canonization.

## 🔧 Core Component: `ValidatorEngine`

```python
from validation.validator import ValidatorEngine

# Validate insight
is_valid = ValidatorEngine.validate_insight(agent, insight, parent_insight, policy_path="circles/circle-policy.yaml")

# Check if ready for canonization
can_canonize = ValidatorEngine.validate_canonization(agent, insight, policy_path="circles/circle-policy.yaml")
```

---

## 🔁 Example Policy (circle-policy.yaml)

```yaml
circle_id: validator-circle-001

require_layer_progression: true        # L3 → L4 is OK, not L3 → L2
allow_same_emotion: false              # e.g., grief → grief not allowed
required_validator_role: validator     # must be validator to vote

allowed_canonizers:
  - validator                          # only validators can canonize

minimum_depth: 2                       # remix trail must be at least 2 layers deep
require_divergence_score: 0.3          # remix must be meaningfully different
```

---

## 🧪 Tests

Run:
```bash
python tests/test_validator.py
```

Verifies:
- Validation rules by role, layer, emotion
- Canonization criteria like divergence and trail depth
