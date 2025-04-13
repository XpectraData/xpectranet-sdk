# 🧠 XpectraNet SDK

A symbolic cognition SDK for building memory-rich autonomous agents.  
Supports remixable insights, trust-based validation, and protocol-aligned governance — backed by decentralized storage and XPDT staking.

---

## 🚀 What It Does

- 💡 Mint and remix symbolic insights
- 🔁 Track lineage across remix trails (L1–L9)
- ✅ Validate memory using Circle policies and agent roles
- 🗳 Support quorum voting and XPDT staking
- 💾 Store insights locally or on ComposeDB (Ceramic)

---

## 📦 Modules

| Layer             | Folder            | Purpose                                  |
|-------------------|-------------------|------------------------------------------|
| Agents            | `agents/`         | Mint, remix, and model symbolic cognition |
| Remix Engine      | `remix/`          | Apply motivation and remix rules         |
| Symbolic Memory   | `memory/`         | Store insights, build trails, persist to Ceramic |
| Validation        | `validation/`     | Apply CirclePolicy rules (L6–L7)         |
| Governance Rules  | `circles/`        | Canonization, role gating, policy YAML   |
| XPDT Logic        | `protocol/`       | Stake threshold + reward distribution    |
| ComposeDB Schema  | `compose/`        | GraphQL model + deploy instructions      |

---

## 🔧 Install

```bash
pip install -r requirements.txt
```

---

## 🧪 Example Usage

```python
from agents.symbolic_agent import SymbolicAgent
agent = SymbolicAgent(glyph="ψ-Echo", remixMotivation="diverge")
origin = agent.mint_insight("The future is undefined.")
```

```python
from remix.remix_engine import RemixEngine
remix = RemixEngine.remix(agent, origin)
```

```python
from validation.validator import ValidatorEngine
ValidatorEngine.validate_insight(agent.to_dict(), remix, origin)
```

---

## 📚 Documentation

See the organized [documentation index](docs/README.md) for:

- ✅ [Formal specs](docs/specs/xko-layers.md) on symbolic layers, governance, and memory
- 🔄 [Usage guides](docs/guides/usage.md) for LangGraph integration and agent lifecycle
- 🧱 [Architecture overview](docs/architecture.md)

---

## 🧪 Run Tests

```bash
python -m unittest discover tests/
```

---

## 🛠 Status

This SDK is in early release. Contributions, extensions, and feedback are welcome.

> Symbolic cognition. Persistent memory. Protocol-aligned intelligence.

---

## 📜 License & Intellectual Property

This SDK is released under the [XPECTRANET™ Protocol License](./LICENSE.md).  

- **XPECTRANET®** is a registered trademark of **Xpectra Data Technologies Ltd.**  
- XPDT, XKO, and symbolic logic (e.g. remix trails, insight scoring, Circle voting) are protected intellectual property.  
- Use in commercial or derivative protocols requires explicit permission.  

> Portions of this codebase are part of a symbolic infrastructure to preserve, evolve, and govern shared cognition.  
> All memory is sacred. Remix with care.
