# 🚀 XpectraNet SDK — Usage Guide

This guide walks you through how to use the XpectraNet SDK to build agents, remix symbolic insights, validate memory, and persist knowledge trails using Ceramic or ComposeDB.

---

## 🔧 Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🤖 Create an Agent

```python
from agents.symbolic_agent import SymbolicAgent

agent = SymbolicAgent(
    glyph="ψ-Echo",
    role="remixer",
    remixMotivation="diverge",
    goal="reveal contradiction"
)
```

---

## 🧠 Mint and Remix Insights

```python
origin = agent.mint_insight("The system is unstable.", layer="L1")

from remix.remix_engine import RemixEngine
remix = RemixEngine.remix(agent, origin)
```

---

## ✅ Validate with Circle Policy

```python
from validation.validator import ValidatorEngine

valid = ValidatorEngine.validate_insight(agent.to_dict(), remix, origin)
```

Use:
- `validate_insight()` → check governance
- `validate_canonization()` → if ready for L7
- `validate_by_quorum()` → multi-agent voting

---

## 🗳 Quorum Voting

```python
votes = [{"affirm": True, "stake": 1.0}, {"affirm": False, "stake": 0.5}]
ValidatorEngine.validate_by_quorum(votes, policy_path="circles/circle-policy.yaml")
```

---

## 💾 Store in Memory or Ceramic

```python
from memory.memory_client import MemoryClient
MemoryClient.store_insight(remix)

from memory.compose_memory import ComposeMemory
ComposeMemory.store(remix)
```

---

## 🧬 Trails

```python
from memory.trail import TrailManager
trail = TrailManager.append(origin["trail"], origin["id"])
```

---

## 📦 Full Loop

See:
- `examples/agent_loop.py`
- `docs/lifecycle.md`
- `docs/circle-governance.md`
- `docs/integration_langgraph.md`

