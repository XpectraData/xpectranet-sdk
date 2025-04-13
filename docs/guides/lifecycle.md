# 🔁 Symbolic Lifecycle Walkthrough

This guide shows how agents co-create, remix, and validate insights across cognitive memory phases using the XpectraNet SDK.

You’ll follow an example loop across three key agents:
- 🧠 `ResearcherAgent` (Mint: L1)
- 🔁 `AnalystAgent` (Remix: L3)
- ✅ `CriticAgent` (Validate: L6)

---

## 🎯 Goal

Demonstrate memory evolution through:

```text
Mint → Remix → Validate → Canonize (optional)
```

Each symbolic act corresponds to a layer in XKO’s cognitive model.

---

## 🧱 Lifecycle Setup

```python
from agents.symbolic_agent import SymbolicAgent
from remix.remix_engine import RemixEngine
from validation.validator import ValidatorEngine
from circles.governance import CirclePolicy
from memory.trail_manager import TrailManager
```

---

## 🧠 Step 1: Mint

```python
researcher = SymbolicAgent(glyph="ψ-Researcher", remixMotivation="curiosity")
origin = researcher.mint_insight("What if time could think?")
```

Output:
- A new insight at `memoryPhase: L1`
- Assigned agent glyph, tone, and tags

---

## 🔁 Step 2: Remix

```python
analyst = SymbolicAgent(glyph="ψ-Analyst", remixMotivation="contrast")
remix = RemixEngine.remix(analyst, origin)
```

This creates:
- A new insight at `memoryPhase: L3`
- Remix lineage pointing to origin

---

## ✅ Step 3: Validate

```python
critic = SymbolicAgent(glyph="ψ-Critic", remixMotivation="affirm")
policy = CirclePolicy.load("circles/circle-policy.yaml")
ValidatorEngine.validate_insight(origin, remix, critic.to_dict(), policy)
```

Validator must:
- Match role/glyph in policy
- Stake minimum XPDT (if required)
- Approve valid transition (e.g. L1 → L3)

---

## 🧭 Step 4: Canonize (Optional)

```python
votes = [critic.to_vote(stake=1.0, intent="affirm")]
ValidatorEngine.validate_canonization(remix, votes, policy)
```

Canonization requires:
- Insight must be in L7 (alias L5)
- Votes must pass quorum

---

## 🧬 Step 5: Extend Trail

```python
trail = TrailManager.build_trail(origin, remix["id"])
print(TrailManager.summarize_trail(trail))
```

---

## 🧠 Cognitive Fingerprint

Each insight carries:

| Field             | Meaning                             |
|------------------|--------------------------------------|
| `memoryPhase`     | XKO Layer (L1, L3, etc.)             |
| `remixMotivation` | Intent for remixing                  |
| `emotion`         | Symbolic emotional context           |
| `tone`, `tags`    | Optional metadata for traceability   |

---

## 🔗 Full Demo Loop

You can automate this loop using LangGraph or in a script.

See:
- [`integration_langgraph.md`](integration_langgraph.md)
- [`trail_manager.py`](../../memory/trail_manager.py)

---

## 🧪 Next

Try customizing:

- Agent emotions + remix rules
- Circle policies with permissions
- Stake-weighted validation

And evolve your own symbolic cognition trail.
