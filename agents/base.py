import yaml
from pathlib import Path

class Agent:
    def __init__(self, glyph, emotion, role, goal):
        self.glyph = glyph
        self.emotion = emotion
        self.role = role
        self.goal = goal

    @classmethod
    def from_yaml(cls, path):
        with open(Path(path)) as f:
            config = yaml.safe_load(f)
        return cls(
            glyph=config.get("glyph"),
            emotion=config.get("emotion"),
            role=config.get("role"),
            goal=config.get("goal")
        )

    def __repr__(self):
        return f"<Agent {self.glyph} | {self.emotion}, {self.role}, {self.goal}>"
