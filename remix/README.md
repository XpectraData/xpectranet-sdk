# `remix/` — Symbolic Remix Engine

This module defines symbolic transformation logic used by agents in the XpectraNet SDK.  
It enables dynamic remixing of memory based on motivation or emotion.

## 🔁 Key Component: `RemixEngine`

This class provides:
- `remix()`: Applies symbolic transformation and returns a new insight
- `_apply_motivation_filter()`: Changes content based on remix intent
- `_calculate_divergence()`: Scores symbolic change from original content

### Supported Motivations

| Motivation   | Effect Description |
|--------------|--------------------|
| `diverge`    | Adds cognitive dissonance |
| `amplify`    | Emphasizes importance |
| `harmonize`  | Frames content within consensus |
| `invert`     | Reverses logic (for contrast) |
| _fallback_   | General remix note if undefined |

## 📦 Usage

The `RemixEngine` is designed to be called inside `agent.remix_insight()` logic.  
It’s plug-and-play for LangGraph workflows or standalone symbolic simulations.

## 🧪 Testing

Run `test_remix_engine.py` from the `/tests` folder to validate remix behavior.

---

Part of the evolving symbolic cognition framework of **XpectraNet**.
