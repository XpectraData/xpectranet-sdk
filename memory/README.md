# 🧠 memory/ — Symbolic Memory Layer for XpectraNet

This module manages insight lineage (trails), in-memory storage, and decentralized persistence via ComposeDB on Ceramic.

---

## ✨ Key Components

| File                | Purpose                                 |
|---------------------|-----------------------------------------|
| `trail_manager.py`  | Manages insight lineage using trails    |
| `memory_client.py`  | Stores insights in in-memory list       |
| `compose_memory.py` | Reads/writes insights via ComposeDB     |

---

## 🔁 TrailManager

```python
TrailManager.append(existing_trail, parent_id)
```
Appends a parent insight ID to build remix lineage.

---

## 📦 MemoryClient

```python
MemoryClient.store_insight(insight)
MemoryClient.get_insights()
MemoryClient.clear_insights()
```
A basic, local-only memory buffer — useful for unit testing or dry runs.

---

## 🌐 ComposeMemory (Ceramic)

```python
from memory.compose_memory import ComposeMemory

doc_id = ComposeMemory.store(insight)
retrieved = ComposeMemory.retrieve(doc_id)
```

Persists symbolic insights to a decentralized ComposeDB graph. Requires a running Ceramic node and GraphQL model schema.

- `store(insight: dict)` → Writes to ComposeDB
- `retrieve(id: str)` → Fetches stored content
- All requests use HTTP POST and return structured JSON

---

## 🔐 Authentication Note

For production environments, ComposeDB requires authenticated DID sessions for mutations.  
Check the [Ceramic Auth Docs](https://developers.ceramic.network/) to set up secure identity integration.

