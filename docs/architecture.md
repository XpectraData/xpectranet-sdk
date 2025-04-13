# 🧱 XpectraNet SDK Architecture

This document outlines the core architecture of the SDK — showing how symbolic insights evolve through modular components.

---

## 🧠 Key Concepts

| Term               | Meaning                                                 |
|--------------------|---------------------------------------------------------|
| Insight            | A symbolic memory unit carrying layer, intent, trail    |
| Memory Phase       | XKO Layer (L0–L9), aliased to operational (L0–L6)       |
| Agent              | An entity (human or LLM-driven) that mints/remixes      |
| Circle             | Governance unit defining who can remix/validate/canonize|
| Trail              | Linked list of insight IDs showing remix lineage        |
| XPDT               | Token used for staking, access, and symbolic scoring    |

---

## 📦 Module Overview

| Folder         | Role                                 |
|----------------|--------------------------------------|
| `agents/`      | Models cognitive agents (`glyph`, `emotion`, `goal`)  
| `remix/`       | Applies symbolic remix transformations and motivations  
| `validation/`  | Validates memory phase transitions and quorum logic  
| `memory/`      | Persists insights, manages trails, connects to ComposeDB  
| `circles/`     | Loads CirclePolicy from YAML (governance + roles)  
| `protocol/`    | Manages XPDT staking, voting, and reward rules  
| `compose/`     | GraphQL schema used by ComposeDB (insight model)

---

## 🔁 Symbolic Lifecycle Flow

```text
Mint (L1) 
  → Remix (L2–L3) 
    → Validate (L4)
      → Canonize (L5) 
        → Archive (L6)
```

Each step:
- Stamps intent, emotion, and fingerprint
- Adds to memory trail
- Can be governed by `circle-policy.yaml`

---

## 🧬 How It Connects

```text
LangGraph Node
   ↳ SymbolicAgent (mint, remix)
       ↳ RemixEngine → ValidatorEngine
           ↳ TrailManager → ComposeDB
```

---

## 🧠 Symbolic Cognition Loop

| Phase      | Agent Role   | Engine Used        |
|------------|--------------|--------------------|
| Mint       | Originator   | SymbolicAgent      |
| Remix      | Analyst      | RemixEngine        |
| Validate   | Critic       | ValidatorEngine    |
| Canonize   | Circle       | QuorumEngine       |

---

## 🔐 Circle Governance

- Loads from `circles/circle-policy.yaml`
- Applies `layerAliases`, `allowedTransitions`, and `validators`
- Enforced in `ValidatorEngine.validate_insight()` and `validate_canonization()`

---

## 🔗 Data Persistence (Optional)

- `memory/compose_client.py` supports ComposeDB
- Maps `xko:Insight` fields to `schema.graphql`
- Can be queried via GraphQL or DIDs

---

For full symbolic context:  
📘 [`spec-xko-layers.md`](specs/spec-xko-layers.md)  
🛠 [`usage.md`](guides/usage.md)
