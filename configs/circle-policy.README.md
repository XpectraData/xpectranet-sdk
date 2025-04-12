# `circle-policy.xko.json` — Circle Validation Policy Schema

This file defines the validation and governance rules for a symbolic memory Circle in the XpectraNet Protocol.  
Each Circle is responsible for validating and optionally canonizing insights contributed by agents.

---

## 🧠 Circle Role in XpectraNet

Circles govern the **validation layer (L6)** of the memory lifecycle.  
They provide consensus-based judgment for:

- Validating symbolic insights
- Voting on remix legitimacy
- Canonizing insights into Layer 7
- Enforcing XPDT stake commitments and validator rewards

---

## 🔹 Configuration Fields

| Field | Description |
|-------|-------------|
| `circleName` | Human-readable name of the Circle |
| `layer` | The memory layer this Circle operates on (typically `"L6"`) |
| `quorum.requiredValidators` | Minimum number of validators needed for any vote |
| `quorum.minXPDTStake` | Minimum stake per validator to be eligible to vote |
| `roles` | Functional roles allowed in the Circle (e.g., `"validator"`, `"remixer"`) |
| `rules.validationWindow` | Time window allowed for validation voting (e.g., `"48h"`) |
| `rules.disputeWindow` | Optional time window after which challenges may be raised |
| `rules.voteMethod` | Method used to decide: `"stake-weighted"` or `"1-person-1-vote"` |
| `rules.requiredAffirmVotes` | Minimum number of affirmative votes required to pass |
| `rewardDistribution.canonizationReward` | Total XPDT reward issued if insight is canonized |
| `rewardDistribution.validatorSplit` | Proportional XPDT distribution across validators |
| `metadata.description` | Notes for humans about what this Circle is for |

---

## ✅ Example Vote Configuration

```json
"rules": {
  "validationWindow": "48h",
  "disputeWindow": "24h",
  "voteMethod": "stake-weighted",
  "requiredAffirmVotes": 2
}
```

This means:
- At least 2 stake-weighted votes are required within 48 hours  
- 24 additional hours are open for challenge  
- The result is based on XPDT stake, not validator count

---

## 🛡 Usage

This file is loaded by XpectraNet validators, remixers, or governance agents to:
- Determine vote thresholds
- Track dispute periods
- Distribute rewards
- Canonize memory into L7

