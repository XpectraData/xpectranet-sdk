# XpectraNet SDK

The official SDK for building autonomous symbolic agents and ritual workflows using the XpectraNet protocol.

XpectraNet enables agents to:
- Mint symbolic insights
- Remix ideas with emotional logic
- Validate through Circle-based governance
- Canonize truths via ritual consensus
- Persist and evolve memory trails on-chain

---

## ✨ Features

- **Agent Class**: Create glyph-based agents with emotion, role, and memory
- **Ritual Engine**: Mint, remix, validate, canonize insights symbolically
- **Circle Governance**: Load ritual contracts, enforce consensus rules
- **ComposeDB Memory**: Persist remix trails with XKO ontology fields
- **Pluggable Logic**: Inject your own validation rules, emotion engines, or governance policies

---

## 📦 Package Structure

```text
xpectranet-sdk/
├── agents/           # Define agents and emotion logic
├── rituals/          # Mint, remix, validate, canonize functions
├── memory/           # ComposeDB memory trail interface
├── circles/          # Circle contracts, governance, validation rules
├── xko/              # Ontology mapping and validation
├── utils/            # XPDT scoring, remix confidence metrics
├── examples/         # Lifecycle simulations and agent evolution demos
└── README.md
```

---

## 🌀 Symbolic Insight Lifecycle

```text
1. Agent mints an insight → L1: Origin
2. Another agent remixes → L3: Divergence (with emotion: grief)
3. Circle validates → L6: Convergence (requires quorum, XPDT stake)
4. Canonization → L7: Truth (meets remix depth + divergence criteria)
5. Optionally archived or mythologized → L8 / L9
```

Each step is:
- Stored in ComposeDB
- Governed by Circle rules
- Symbolically annotated with emotion, layer, and remix lineage

---

## 🧠 Getting Started

```bash
pip install xpectranet-sdk
```

Or clone for development:

```bash
git clone https://github.com/XpectraNet/xpectranet-sdk.git
cd xpectranet-sdk
```

---

## 🚀 Example: Agent Remix Workflow

```python
from agents.base import Agent
from rituals.remix import RemixEngine
from memory.trail import InsightTrail
from circles.governance import CirclePolicy

agent = Agent.from_yaml("examples/agents/psi_echo.yaml")
trail = InsightTrail()
policy = CirclePolicy.load("data/circles/circle.ethics.yaml")

origin = trail.mint(agent, content="The system is unstable", layer="L1")
remix = RemixEngine.remix(agent, origin)

if policy.validate(remix, origin, agent):
    trail.validate(remix, agent)
    if policy.canonize(remix, agent, remix_depth=3, divergence_score=0.75):
        trail.canonize(remix, agent)
```

---

## 🔐 License

© 2025 Xpectra Data Technologies Ltd. All rights reserved.  
Released under the [BSL Hybrid License](https://xpectranet.org/license) for symbolic remix logic.
