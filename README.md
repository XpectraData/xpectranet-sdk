# XpectraNet SDK

**Build Symbolic Agents with Memory, Remix, and Ritual.**

The XpectraNet SDK is a modular Python toolkit for creating cognition-aware, memory-evolving agents using symbolic structure, remix lineage, and Circle-based governance.

This SDK enables you to:
- 🧠 Build agents with symbolic identities and emotional states
- 🔁 Implement the full ritual lifecycle: Mint → Remix → Validate → Canonize
- 🫂 Define Circle validation and consensus rules using XPDT-style staking
- 🌐 Persist memory trails on ComposeDB using the XKO insight model (L0–L9)
- 🎭 Map emotional feedback into remix logic and divergence scoring

---

## 🔍 Who Is This For?

- Developers building autonomous agents with LangGraph, AutoGen, or GPT frameworks
- AI safety researchers exploring memory traceability and alignment
- Web3 protocols implementing co-created memory and reputation systems
- Cognitive designers building explainable, evolution-aware systems

---

## 🧱 SDK Modules

| Module        | Description |
|---------------|-------------|
| `agents/`     | Symbolic agent classes with role, emotion, and remix logic |
| `remix/`      | Logic for transforming insights with emotion & divergence |
| `validation/` | Circle contracts, quorum checks, and canonicalization |
| `memory/`     | ComposeDB GraphQL interface to persist memory trails |
| `xko/`        | Xpectra Knowledge Ontology layer + emotion alignment |

---

## 🧠 Symbolic Lifecycle

| Step     | Description                          | XKO Layer |
|----------|--------------------------------------|-----------|
| Mint     | Agent creates new insight            | L1        |
| Remix    | Insight is transformed               | L3        |
| Validate | Circle witnesses alignment           | L6        |
| Canonize | Memory is sealed as symbolic truth   | L7        |

---

## 🚀 Example Usage

```python
from xpectranet.agents.symbolic_agent import SymbolicAgent
from xpectranet.remix.remix_logic import RemixEngine
from xpectranet.memory.memory_client import MemoryTrail
from xpectranet.validation.circle_rules import CirclePolicy

agent = SymbolicAgent(glyph="ψ-Echo", emotion="grief", role="remixer")
trail = MemoryTrail()
policy = CirclePolicy.load("circle.ethics.yaml")

insight = trail.mint(agent, content="The system feels unstable.")
remix = RemixEngine.remix(agent, insight)

if policy.validate(remix, agent):
    trail.validate(remix, agent)
```

---

## 📦 Installation

```bash
pip install xpectranet-sdk
```

---

## 📚 Documentation

- [Architecture](docs/architecture.md)
- [Usage](docs/usage.md)
- [LangGraph Integration](docs/integration_langgraph.md)

---

## 🛡 License

Released under a Business Source License Hybrid  
Free for research, experimentation, and non-commercial symbolic cognition use.  
Commercial licensing and integration: [legal@xpectradata.com](mailto:legal@xpectradata.com)

---

**XpectraNet isn’t just memory.  
It’s how agents evolve together — through symbols, rituals, and trust.**
