# 🧩 LangGraph Integration with XpectraNet SDK

This document explains how to integrate symbolic memory and governance layers from the XpectraNet SDK into LangGraph agent workflows.

---

## 🧠 What LangGraph Solves

LangGraph enables:
- Multi-agent task orchestration
- Message passing between nodes
- Shared memory state across iterations

---

## 🤝 What XpectraNet Adds

By integrating with the SDK, LangGraph agents can:
- Mint and remix symbolic insights
- Track memory trails and divergence
- Validate insights using Circle policy rules
- Store and query symbolic memory (via ComposeDB)

---

## 🔁 Agent Workflow Overview

```text
L1: mint_insight()      → Researcher agent
L3: remix_insight()     → Analyst agent
L6: validate_insight()  → Critic agent
L7: canonize()          → (optional, if Circle rules met)
```

Each phase uses:
- `SymbolicAgent`
- `RemixEngine`
- `ValidatorEngine`
- `TrailManager`
- `MemoryClient` or `ComposeMemory`

---

## ⚙️ Sample LangGraph Hook

```python
def remix_hook(state):
    parent = state["insight"]
    agent = state["agent"]
    remix = RemixEngine.remix(agent, parent)
    state["remix"] = remix
    return state
```

---

## 💾 Persistent Memory

Use either:
```python
MemoryClient.store_insight(insight)         # for mock/in-memory tests
ComposeMemory.store(insight)                # for ComposeDB on Ceramic
```

---

## 🧪 Validation Example

```python
valid = ValidatorEngine.validate_insight(agent.to_dict(), remix, parent)
if valid:
    MemoryClient.store_insight(remix)
```

---

## 🌐 ComposeDB Storage Flow

1. Define model (`compose/schema.graphql`)
2. Deploy using `composedb` CLI
3. Use `ComposeMemory.store()` to persist

---

## 🔄 Loop Option

Combine LangGraph's looping engine with:
- `agent_config.json` (remix triggers)
- `ValidatorEngine.validate_by_quorum()` for collective votes
- `TrailManager` for remix lineage tracking

---

## 📦 See Also

- `examples/agent_loop.py`
- `tests/test_validator_quorum.py`
- `protocol/staking.py` + `quorum.py`
