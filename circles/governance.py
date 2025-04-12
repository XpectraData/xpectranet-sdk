import yaml
from pathlib import Path

class CirclePolicy:
    def __init__(self, policy_dict):
        self.rules = policy_dict.get("ritual_rules", {})
        self.circle_id = policy_dict.get("circle_id")

    @classmethod
    def load(cls, path):
        with open(Path(path)) as f:
            data = yaml.safe_load(f)
        return cls(data)

    def validate(self, insight, parent, agent):
        remix = self.rules.get("remix", {})
        if remix.get("require_layer_progression", False):
            if insight.get("layer") <= parent.get("layer"):
                return False
        if remix.get("allow_same_emotion") is False:
            if insight.get("emotion") == parent.get("emotion"):
                return False
        return True

    def canonize(self, insight, agent, remix_depth, divergence_score):
        canon = self.rules.get("canonize", {})
        if remix_depth < canon.get("minimum_depth", 3):
            return False
        if divergence_score < canon.get("require_divergence_score", 0.7):
            return False
        return True
