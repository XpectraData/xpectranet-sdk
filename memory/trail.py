class InsightTrail:
    def __init__(self):
        self.store = []

    def mint(self, agent, content, layer="L1"):
        insight = {
            "content": content,
            "layer": layer,
            "emotion": agent.emotion,
            "glyph": agent.glyph,
            "agent": agent.__dict__,
            "trail": []
        }
        self.store.append(insight)
        return insight

    def validate(self, insight, agent):
        insight["validated_by"] = agent.glyph
        insight["layer"] = "L6"
        return insight

    def canonize(self, insight, agent):
        insight["canonical"] = True
        insight["canonized_by"] = agent.glyph
        insight["layer"] = "L7"
        return insight
