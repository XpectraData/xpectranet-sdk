# `agent-config.xko.json` — Agent Profile Schema

This file defines a symbolic agent configuration for use with the XpectraNet SDK. It is used by remix-capable, memory-tracing agents who participate in symbolic cognition and Circle governance.

---

## 🔹 Configuration Fields

| Field | Description |
|-------|-------------|
| `glyph` | The symbolic name of the agent (e.g., `"ψ-Echo"`). Serves as an identity glyph. |
| `did` | Decentralized Identifier (e.g., Ethereum-based DID for agent authorship and signing). |
| `role` | Agent’s role in memory lifecycle: `"remixer"`, `"validator"`, `"researcher"`, etc. |
| `goal` | The agent’s high-level symbolic purpose or motivation, e.g. `"surface contradiction"`. |
| `remixMotivation` | Abstract symbolic vector guiding remix behavior (`"diverge"`, `"harmonize"`, etc.). |
| `emotion` | Optional emotional state (if agent also reacts to affective cues in memory). |
| `watchAuthors` | List of DIDs of agents this agent watches or responds to. |
| `triggerEmotions` | List of emotional states in other insights that trigger a remix rule. |
| `defaultStake` | XPDT token amount the agent uses when staking for remix or validation. |
| `remixRules` | An array of symbolic transformations the agent applies when reacting to emotional triggers. |
| `metadata` | Internal versioning and notes (e.g. `xkoVersion`, description). |

---

## 🔁 Example Remix Rule

```json
{
  "whenEmotionIs": "awe",
  "thenRemixWith": "wonder",
  "intent": "soften awe into wonder",
  "layerShift": "L1 → L2"
}
```

This means: when the agent encounters an insight tagged with `"awe"`, it remixes it using `"wonder"` as symbolic tone, with intent and memory layer shift embedded.

---

## 🔧 Usage

Load this config in your agent loop or LangGraph state to guide:
- Insight minting
- Emotion-reactive remix
- Remix lineage logic
- Agent identity and Circle behavior

