# 🧬 compose/ — Insight Schema for ComposeDB

This folder defines the GraphQL schema for symbolic insights on the Ceramic ComposeDB network.

---

## 📄 File: `schema.graphql`

The `Insight` model includes:

| Field             | Description                                              |
|------------------|----------------------------------------------------------|
| `content`         | Required string holding the insight content             |
| `layer`           | Symbolic memory layer (L0–L9)                            |
| `remixOf`         | DID of parent insight (if remixed)                      |
| `remixMotivation` | Reason for remix (e.g., diverge, harmonize, amplify)    |
| `validatedBy`     | List of DIDs that validated the insight                 |
| `canonized`       | True if insight was accepted into Layer 7 (Canon)       |
| `trail`           | List of insight IDs forming remix lineage               |
| `divergenceScore` | Float score representing remix difference               |
| `tags`            | Optional symbolic tags                                  |
| `createdAt`       | Auto-generated timestamp                                |

---

## 🚀 Deploying the Schema

To publish this model on ComposeDB:

```bash
npx @composedb/cli@latest model:compile compose/schema.graphql
npx @composedb/cli@latest model:deploy ./schema-runtime.json
```

You must:
- Have a running Ceramic node
- Be authenticated with a DID
- Configure your ComposeDB CLI

---

## 🔗 Docs

Learn more:  
👉 https://developers.ceramic.network/build/compose/

