"""

ValidatorEngine — Validates symbolic insight transitions using layer aliasing and Circle rules.

This engine uses the XKO simplified layer model (7-layer alias mapping)
to enforce meaningful transitions between symbolic memory phases (L0–L9 → L0–L6).
"""

from typing import Dict, List
from circles.governance import CirclePolicy
from protocol.quorum import QuorumEngine

class ValidatorEngine:
    LAYER_ALIAS_MAP = {
        "L0": "L0",
        "L1": "L1",
        "L2": "L2",
        "L3": "L2",
        "L4": "L3",
        "L5": "L3",
        "L6": "L4",
        "L7": "L5",
        "L8": "L6",
        "L9": "L6"
    }

    ALLOWED_TRANSITIONS = [
        ("L1", "L2"),
        ("L2", "L3"),
        ("L3", "L4"),
        ("L4", "L5"),
        ("L5", "L6")
    ]

    @staticmethod
    def get_alias(layer: str) -> str:
        return ValidatorEngine.LAYER_ALIAS_MAP.get(layer, layer)

    @staticmethod
    def is_valid_transition(from_layer: str, to_layer: str) -> bool:
        alias_from = ValidatorEngine.get_alias(from_layer)
        alias_to = ValidatorEngine.get_alias(to_layer)
        return (alias_from, alias_to) in ValidatorEngine.ALLOWED_TRANSITIONS

    @staticmethod
    def validate_transition(insight_from: Dict, insight_to: Dict) -> bool:
        layer_from = insight_from.get("memoryPhase")
        layer_to = insight_to.get("memoryPhase")
        if not ValidatorEngine.is_valid_transition(layer_from, layer_to):
            raise ValueError(
                f"Invalid transition: {layer_from} → {layer_to} "
                f"(alias: {ValidatorEngine.get_alias(layer_from)} → {ValidatorEngine.get_alias(layer_to)})"
            )
        return True

    @staticmethod
    def validate_with_circle_policy(insight_from: Dict, insight_to: Dict, policy: CirclePolicy, agent: Dict) -> bool:
        ValidatorEngine.validate_transition(insight_from, insight_to)
        if not policy.can_validate(agent):
            raise PermissionError("Agent lacks permission to validate based on CirclePolicy.")
        return True

    @staticmethod
    def validate_with_quorum(insight_id: str, agent_votes: List[Dict], policy: CirclePolicy) -> bool:
        quorum = QuorumEngine(policy)
        return quorum.evaluate(insight_id, agent_votes)

    @staticmethod
    def validate_insight(insight_from: Dict, remix_insight: Dict, agent: Dict, policy: CirclePolicy) -> bool:
        """
        High-level validation method for regular insight transition.

        Args:
            insight_from (dict): The original insight that the new one remixes.
                Must contain at least a `memoryPhase` key.
            remix_insight (dict): The new symbolic insight to be validated.
                Should contain its intended `memoryPhase` for transition checking.
            agent (dict): The validating agent's identity and context.
                Must include role and glyph, and optionally XPDT stake.
            policy (CirclePolicy): The governing Circle ruleset.
                Defines what transitions and roles are permitted.

        Returns:
            bool: True if validation passes both transition and permission rules.
        Raises:
            ValueError: If symbolic memory transition is not allowed.
            PermissionError: If agent lacks permission based on CirclePolicy.
        """
        return ValidatorEngine.validate_with_circle_policy(insight_from, remix_insight, policy, agent)

    @staticmethod
    def validate_canonization(insight: Dict, votes: List[Dict], policy: CirclePolicy) -> bool:
        """
        High-level validation method for canonization phase.

        Args:
            insight (dict): The insight proposed for canonization.
                Must contain `memoryPhase` set to "L7" (canonical layer) and a unique `id`.
            votes (list of dict): List of agent votes for or against canonization.
                Each vote dict typically includes:
                    - `stake` (float): XPDT amount or influence weight.
                    - `glyph` (str): The identity or symbolic role of the validator.
                    - `intent` (str): Optional rationale or symbolic purpose for the vote.
            policy (CirclePolicy): The Circle governance policy object.
                Contains quorum rules, stake requirements, and authorized roles.

        Returns:
            bool: True if quorum is met and the insight is eligible for canonization.
        Raises:
            ValueError: If the insight is not in the canonical memory layer.
        """
        return ValidatorEngine.validate_with_quorum(insight.get("id", ""), votes, policy)
