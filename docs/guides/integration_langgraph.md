# 🔗 LangGraph Integration with XpectraNet SDK

This guide shows how to integrate LangGraph workflows with XpectraNet's symbolic memory system.

Use this to:
- 🧠 Orchestrate agents using LLMs that co-evolve symbolic insight
- 🔁 Mint, remix, validate, and canonize insights as memory trails
- 🗳 Collaborate using Circle-based governance and XPDT staking

---

## ⚙️ Stack Overview

| Layer             | Tool         | Purpose                                |
|------------------|--------------|----------------------------------------|
| Agent Workflow    | LangGraph    | LLM-based orchestration of agent roles |
| Symbolic Memory   | XpectraNet   | Layered cognition, insight evolution   |
| Storage Layer     | ComposeDB    | Persistent decentralized memory graph  |
| Identity + Access | Ceramic      | Agent DIDs, access control, authorship |

---

## 🧱 How It Works

1. 🧠 `SymbolicAgent` runs in LangGraph node with prompt + intent config  
2. 💡 `mint_insight()` or `remix_insight()` is called with symbolic parameters  
3. 🔗 Trail is extended via `TrailManager.build_trail()`  
4. ✅ Transition is checked via `ValidatorEngine.validate_insight()`  
5. 💾 Result is persisted via `memory/compose_client.py` to ComposeDB

---

## 📘 Sample Agent Loop (L1 → L3 → L6)

```python
from agents.symbolic_agent import SymbolicAgent
from remix.remix_engine import RemixEngine
from validation.validator import ValidatorEngine
from memory.trail_manager import TrailManager

# Step 1: Mint a new insight
agent = SymbolicAgent(glyph="ψ-Echo", remixMotivation="diverge")
origin = agent.mint_insight("What if memory had emotion?")

# Step 2: Remix it with new emotional context
remix = RemixEngine.remix(agent, origin)

# Step 3: Validate the transformation
ValidatorEngine.validate_insight(origin, remix, agent.to_dict(), policy)

# Step 4: Extend the trail
trail = TrailManager.build_trail(origin, remix["id"])
```

---

## 🔧 Config Tips

- Agents can be configured using `agent-config.xko.json` with:
  - `glyph`, `defaultStake`, `remixRules`, `emotionMap`, etc.

- Circle rules loaded via `CirclePolicy.load(path)`
- Stake logic via `XPDTStaking.calculate_rewards()`

---

## 🧠 Supported Symbolic Concepts

| Feature           | Description                                 |
|------------------|---------------------------------------------|
| `memoryPhase`     | XKO Layer (L0–L9) of the current insight    |
| `remixMotivation` | Reason for symbolic transformation          |
| `emotion`, `tone`, `perspective` | Agent fingerprint for traceability |
| `trail`           | Ordered list of remix lineage               |

---

## 🧩 Use Cases

- 🤖 Multi-agent LangGraph pipelines with symbolic memory state
- 🧠 Simulated cognition loops for AI alignment or dialogue trails
- 🧬 Memory trace analysis for governance and remix lineage

---

## 📦 Coming Soon

- LangGraph templates for `Remixer`, `Validator`, `Canonizer`
- Node utilities for Circle-based remix chains
- XPDT token integration for role gating and trail scoring

---

For full schema and examples, visit:  
📚 [`compose/schema.graphql`](../../compose/schema.graphql)  
📘 [`docs/specs/spec-xko-layers.md`](../specs/spec-xko-layers.md)  
🔄 [`docs/guides/lifecycle.md`](lifecycle.md)

