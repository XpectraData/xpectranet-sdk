"""
CirclePolicy — Loads and applies validation rules from Circle YAML policy.

Supports alias-aware layer validation and role-based permission logic.
"""

import os
import yaml
from typing import Dict, List
from pathlib import Path

class CirclePolicy:
    def __init__(self, config: Dict):
        self.config = config
        self.min_stake = self.config.get("minStake", 1.0)
        self.allowed_transitions = {
            (t["from"], t["to"]) for t in self.config.get("allowedTransitions", [])
        }
        self.layer_aliases = self.config.get("layerAliases", {})
        self.validators = self.config.get("validators", [])

    def get_alias(self, layer: str) -> str:
        """Maps any L0–L9 layer to its alias form (L0–L6)."""
        return self.layer_aliases.get(layer, layer)

    def is_transition_allowed(self, from_layer: str, to_layer: str) -> bool:
        """Checks if the transition (after alias mapping) is allowed per policy."""
        alias_from = self.get_alias(from_layer)
        alias_to = self.get_alias(to_layer)
        return (alias_from, alias_to) in self.allowed_transitions

    def can_validate(self, agent: Dict) -> bool:
        """Determines if an agent has validation rights."""
        for validator in self.validators:
            if validator["role"] == agent.get("role") and validator["glyph"] == agent.get("glyph"):
                return "canValidate" in validator.get("permissions", [])
        return False

    def can_canonize(self, agent: Dict) -> bool:
        """Determines if an agent has canonization rights."""
        for validator in self.validators:
            if validator["role"] == agent.get("role") and validator["glyph"] == agent.get("glyph"):
                return "canCanonize" in validator.get("permissions", [])
        return False

    def can_remix(self, agent: Dict) -> bool:
        """Determines if an agent has remix rights."""
        for validator in self.validators:
            if validator["role"] == agent.get("role") and validator["glyph"] == agent.get("glyph"):
                return "canRemix" in validator.get("permissions", [])
        return False

    @classmethod
    def load(cls, path: str = None):
        """
        Load governance policy from a YAML file.

        Args:
            path (str): Path to the YAML policy config file.

        Returns:
            CirclePolicy: A new policy instance with the loaded rules.
        """
        # Allow environment variable fallback for path
        path = path or os.getenv("XKO_POLICY_PATH", "circles/circle-policy.yaml")
        policy_path = Path(path)
        with policy_path.open("r", encoding="utf-8") as f:
            config = yaml.safe_load(f)
        return cls(config)
