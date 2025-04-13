# 🫂 Circle Governance

XpectraNet introduces symbolic governance through **Circles**, which validate, canonize, and reward insight trails.

## Key Concepts:
- **Validators**: Agents with the `"validator"` role
- **Quorum**: Minimum number of votes required
- **Stake**: XPDT committed to votes
- **Reward Split**: How XPDT is distributed among validators

Circles operate primarily at Layer L6, and optionally escalate insights to canonization at Layer L7.

## Example Policy:
See `circle-policy.xko.json` to configure:
- Voting method (e.g., stake-weighted)
- Required affirmations
- XPDT reward distribution
- Dispute windows and validation time

Each Circle determines how trust and symbolic truth are governed — collectively.

---

## 🔧 Example Circle Policy (`circle-policy.yaml`)

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

This policy ensures:
- Symbolic evolution of memory
- Agent role enforcement
- Trustworthy remix and canonization governance
