from typing import Dict, Optional
import uuid
from .base_agent import BaseAgent  # Import the abstract base class

class SymbolicAgent(BaseAgent):
    """
    A symbolic cognition agent designed for LangGraph-style workflows.

    This agent supports either an emotional state (e.g., "grief", "awe") or a symbolic remix motivation
    (e.g., "diverge", "harmonize", "amplify") to guide how insights are minted and transformed.

    It can generate new insights (minting) or remix existing ones with lineage tracking.
    """

    def __init__(self, glyph: str, role: str, emotion: Optional[str] = None,
                 remixMotivation: Optional[str] = None, goal: Optional[str] = None):
        """
        Initialize a symbolic agent with a glyph (symbolic ID), role (e.g., 'validator'),
        optional emotional tag, remix motivation, and a goal.

        Args:
            glyph (str): Symbolic name or agent glyph (e.g. 'ψ-Echo').
            role (str): Functional or ritual role (e.g. 'remixer', 'validator').
            emotion (Optional[str]): Emotional state vector (e.g. 'grief').
            remixMotivation (Optional[str]): Symbolic remix intent (e.g. 'diverge').
            goal (Optional[str]): Long-term intent or pursuit (e.g. 'harmonize').
        """
        self.glyph = glyph
        self.role = role
        self.emotion = emotion
        self.remixMotivation = remixMotivation
        self.goal = goal

    def mint_insight(self, content: str, layer: str = "L1") -> Dict:
        """
        Mint a new symbolic insight.

        Args:
            content (str): The insight's primary content.
            layer (str): The symbolic layer (default L1 for original minting).

        Returns:
            Dict: A structured insight dictionary including emotion/motivation and trace metadata.
        """
        return {
            "id": str(uuid.uuid4()),  # unique ID for the insight
            "content": content,
            "layer": layer,
            "emotion": self.emotion,
            "remixMotivation": self.remixMotivation,
            "createdBy": self.glyph,
            "timestamp": datetime.utcnow().isoformat(),
            "agent": self.to_dict(),
            "trail": []  # this is the trail root
        }

    def remix_insight(self, parent_insight: Dict, new_content: str, layer: str = "L3") -> Dict:
        """
        Remix an existing insight with symbolic transformation and preserved lineage.

        Args:
            parent_insight (Dict): The original insight to remix.
            new_content (str): The newly transformed version.
            layer (str): The symbolic layer (default L3 for remix).

        Returns:
            Dict: A new insight object preserving remix lineage and symbolic cues.
        """
        return {
            "id": str(uuid.uuid4()),
            "content": new_content,
            "layer": layer,
            "emotion": self.emotion,
            "remixMotivation": self.remixMotivation,
            "createdBy": self.glyph,
            "remixOf": parent_insight.get("id"),
            "parentEmotion": parent_insight.get("emotion"),
            "timestamp": datetime.utcnow().isoformat(),
            "agent": self.to_dict(),
            "trail": parent_insight.get("trail", []) + [parent_insight.get("id")]
        }

    def to_dict(self) -> Dict:
        """
        Convert the agent state into a serializable dictionary for embedding in insight metadata.

        Returns:
            Dict: Serialized agent information.
        """
        return {
            "glyph": self.glyph,
            "role": self.role,
            "emotion": self.emotion,
            "remixMotivation": self.remixMotivation,
            "goal": self.goal
        }
