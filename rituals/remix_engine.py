from utils.emotion import score_emotion_divergence

class RemixEngine:
    @staticmethod
    def remix(agent, parent_insight):
        remix = {
            "content": "Symbolically reinterpreted: " + parent_insight["content"],
            "emotion": agent.emotion,
            "layer": "L3",
            "glyph": agent.glyph,
            "remixOf": parent_insight,
            "agent": agent.__dict__
        }
        remix["divergence_score"] = score_emotion_divergence(remix["emotion"], parent_insight["emotion"])
        remix["xdo:motivation"] = "xdo:EmotionalContrast"
        return remix
