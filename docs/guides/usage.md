# 🚀 Quick Usage Guide — XpectraNet SDK

This guide walks through the basic building blocks of symbolic cognition using the XpectraNet SDK.

You’ll learn how to:

- 💡 Mint a new insight
- 🔁 Remix and transform memory
- ✅ Validate transitions using Circle policy
- 🛠 Extend memory trails with symbolic fingerprinting

---

## 🔧 1. Setup

Install requirements:
```bash
pip install -r requirements.txt
```

Import key modules:
```python
from agents.symbolic_agent import SymbolicAgent
from remix.remix_engine import RemixEngine
from validation.validator import ValidatorEngine
from circles.governance import CirclePolicy
from memory.trail_manager import TrailManager
```

---

## 🧠 2. Mint a Symbolic Insight

```python
agent = SymbolicAgent(glyph="ψ-Echo", remixMotivation="question")
origin = agent.mint_insight("What if silence was never empty?")
```

Each insight has:
- `content`, `memoryPhase`, `emotion`, `trail`, `tags`, etc.
- Layer L1 (Origin Insight) by default

---

## 🔁 3. Remix Insight with Motivation

```python
remix = RemixEngine.remix(agent, origin)
```

Creates a symbolic transformation:
- Applies remix rules based on emotion/motivation
- Moves insight from L1 → L2 (or beyond)

---

## ✅ 4. Validate Insight Using Circle Policy

```python
policy = CirclePolicy.load("circles/circle-policy.yaml")
ValidatorEngine.validate_insight(origin, remix, agent.to_dict(), policy)
```

Checks:
- Memory layer transition (L1 → L2)
- Agent permissions (via `role` and `glyph`)
- Circle-defined transitions

---

## 🧬 5. Build and Extend the Trail

```python
trail = TrailManager.build_trail(origin, remix["id"])
```

Appends remix to insight lineage.

You can also summarize:
```python
summary = TrailManager.summarize_trail(trail)
print(summary)  # insight:L1 → insight:L2 → insight:L3 ...
```

---

## 🧩 Agent Config (Optional)

Agents can load symbolic config via `agent-config.xko.json`:
```json
{
  "glyph": "ψ-Echo",
  "remixRules": [
    {
      "whenEmotionIs": "grief",
      "thenRemixWith": "curiosity",
      "layerShift": "L0 → L1"
    }
  ],
  "defaultStake": 1.0
}
```

---

## 🔗 Next Steps

- 🛠 Run full loops with LangGraph orchestration  
- 🧠 Explore emotional fingerprints and validation workflows  
- 📚 Dive deeper into [Symbolic Lifecycle](lifecycle.md)

---

## Resources

- [Layer Model](../specs/spec-xko-layers.md)  
- [Circle Governance](../specs/spec-circle-governance.md)  
- [ComposeDB Schema](../../compose/schema.graphql)
