import yaml
from pathlib import Path
import os

class CirclePolicy:
    """
    CirclePolicy defines governance rules for validating and canonizing insights in a Circle.

    It allows for symbolic enforcement of memory evolution — such as requiring emotional diversity,
    layer progression, and divergence before an insight can be canonized into permanent memory.
    """

    def __init__(self, policy_dict: dict):
        self.rules = policy_dict or {}
        self.circle_id = policy_dict.get("circle_id", "default")  # Identifier for multi-circle use

    @classmethod
    def load(cls, path: str):
        """
        Load governance policy from a YAML file.

        Args:
            path (str): Path to the YAML policy config file.

        Returns:
            CirclePolicy: A new policy instance with the loaded rules.
        """
        path = path or os.getenv("XKO_POLICY_PATH", "circles/circle-policy.yaml")
        policy_path = Path(path)
        with policy_path.open("r", encoding="utf-8") as f:
            config = yaml.safe_load(f)
        return cls(config)

    def validate(self, agent: dict, insight: dict, parent_insight: dict) -> bool:
        """
        Validate a symbolic insight based on the Circle's rules.

        Args:
            agent (dict): The agent proposing the validation.
            insight (dict): The new insight being validated.
            parent_insight (dict): The insight it is remixed from.

        Returns:
            bool: True if the insight passes validation according to policy.
        """
        if self.rules.get("require_layer_progression", False):
            parent_layer = parent_insight.get("layer", "")
            new_layer = insight.get("layer", "")
            if new_layer <= parent_layer:
                return False

        if not self.rules.get("allow_same_emotion", True):
            if insight.get("emotion") == parent_insight.get("emotion"):
                return False

        # Example: only allow validators with specific role
        required_role = self.rules.get("required_validator_role")
        if required_role and agent.get("role") != required_role:
            return False

        return True

    def canonize(self, agent: dict, insight: dict) -> bool:
        """
        Determine whether an insight qualifies for canonization.

        Args:
            agent (dict): The agent initiating canonization.
            insight (dict): The candidate insight.

        Returns:
            bool: True if the insight qualifies to be canonized.
        """
        min_score = self.rules.get("require_divergence_score", 0.0)
        if min_score > 0 and insight.get("divergenceScore", 0.0) < min_score:
            return False

        min_depth = self.rules.get("minimum_depth", 0)
        if min_depth > 0 and len(insight.get("trail", [])) < min_depth:
            return False

        # Optional: restrict canonization to certain agent roles
        canon_role = self.rules.get("allowed_canonizers")
        if canon_role and agent.get("role") not in canon_role:
            return False

        return True
