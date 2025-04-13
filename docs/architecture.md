# 🧠 XpectraNet SDK Architecture

This document outlines the symbolic protocol architecture that powers the XpectraNet SDK — a cognitive system for agent memory, remix, validation, and decentralized governance.

---

## 🧩 Layered Overview

```text
Agents
 └── SymbolicAgent (mint, remix)
     └── RemixEngine (apply motivation + score)
         └── TrailManager (build lineage)
         └── ComposeMemory (store in Ceramic)
     └── ValidatorEngine (check governance)
         └── CirclePolicy (YAML-based)
         └── XPDTStaking + QuorumEngine
```

---

## 📦 Module Map

| Layer            | Folder       | Key Functions                                   |
|------------------|--------------|--------------------------------------------------|
| 🧠 Agents        | `agents/`     | Mint/remix insight, run symbolic logic          |
| 🔁 Remix Engine  | `remix/`      | Transform content, assign motivation, score     |
| 🧠 Memory        | `memory/`     | Trail manager, local store, ComposeDB adapter   |
| ✅ Validation    | `validation/` | Agent and quorum rule checks                    |
| 🫂 Governance    | `circles/`    | Circle policies, canonization eligibility       |
| 💠 XPDT Logic    | `protocol/`   | Staking, quorum, symbolic scoring               |
| 📚 Schemas       | `compose/`    | ComposeDB Insight model (GraphQL)               |

---

## 🧠 Symbolic Memory Flow

1. Agent mints origin insight
2. Remix applies symbolic transformation
3. Insight passes Circle validation
4. Canonized insights are elevated to Layer L7
5. Memory is stored locally or in ComposeDB

---

## 🔗 Circle Governance Components

- Circle policy (`circle-policy.yaml`)
- Validator role enforcement
- Layer + emotion gating
- Quorum voting rules (by count or stake)

---

## 🗳 Voting & Staking Integration

- `staking.py`: Ensures XPDT thresholds are met  
- `quorum.py`: Calculates vote outcome  
- Reward splits and trail enrichment

---

## 🧪 Testing

All core modules include:
- Unit tests under `/tests`
- Quorum voting, remix logic, validation

---

## 🧬 Interoperability

- Agents compatible with LangGraph  
- Schema deployable to ComposeDB  
- Insight data exportable as JSONLD

