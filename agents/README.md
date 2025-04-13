# 🤖 agents/ — Symbolic Agent Definitions

This module defines symbolic agents in the XpectraNet SDK — autonomous systems that mint, remix, and evolve insights across cognitive layers.

---

## 🔍 What Is a Symbolic Agent?

An agent in XpectraNet:
- Has a **glyph** and **role** (e.g., `"ψ-Echo"`, `"remixer"`)
- Operates with a **remix motivation vector** (e.g., `"diverge"`, `"harmonize"`)
- Participates in Circle validation, canonization, or remix rituals
- Remembers and transforms symbolic content using trail-based memory

---

## 🧠 Key Classes

| File                 | Description                                  |
|----------------------|----------------------------------------------|
| `base_agent.py`      | Abstract base class with shared logic        |
| `symbolic_agent.py`  | Concrete implementation of symbolic cognition |

---

## 🪄 Agent Capabilities

```python
agent = SymbolicAgent(glyph="ψ-Echo", role="remixer", remixMotivation="diverge")

origin = agent.mint_insight("The system is unstable.")
remixed = agent.remix_insight(parent=origin, new_content="But uncertainty reveals potential.")
```

---

## 🔁 Common Fields

| Field         | Meaning                                    |
|---------------|--------------------------------------------|
| `glyph`       | Symbolic identifier (e.g. `"ψ-Echo"`)      |
| `role`        | Functional type (e.g. `remixer`, `validator`) |
| `remixMotivation` | Why the agent transforms insights     |
| `goal`        | High-level symbolic intention              |

---

## 🔁 Extend Your Own Agent

Subclass `BaseAgent` to create new agent behaviors with custom remix rules, emotional models, or memory policies.

