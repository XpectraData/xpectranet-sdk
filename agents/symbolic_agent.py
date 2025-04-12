from typing import Dict, Optional
import uuid
from datetime import datetime

class SymbolicAgent:
    """
    A symbolic cognition agent designed for use in LangGraph workflows.
    Capable of minting and remixing symbolic insights with emotional context, symbolic identity, and traceable lineage.

    Attributes:
        glyph (str): The symbolic identifier of the agent (e.g., "ψ-Echo").
        emotion (str): The current emotional context (e.g., "awe", "grief").
        role (str): The functional role of the agent (e.g., "researcher", "validator").
        goal (str): The high-level intention or motivational drive (e.g., "harmonize", "diverge").
    """

    def __init__(self, glyph: str, emotion: str, role: str, goal: Optional[str] = None):
        self.glyph = glyph
        self.emotion = emotion
        self.role = role
        self.goal = goal

    def mint_insight(self, content: str, layer: str = "L1") -> Dict:
        """
        Creates a new insight from scratch, initiating a symbolic trail.

        Args:
            content (str): The textual or symbolic content of the insight.
            layer (str): The XKO memory layer of this act (default: L1 = Mint).

        Returns:
            Dict: A dictionary representing the minted insight with agent metadata.
        """
        return {
            "id": str(uuid.uuid4()),  # unique identifier for the insight
            "content": content,
            "layer": layer,
            "emotion": self.emotion,
            "createdBy": self.glyph,
            "timestamp": datetime.utcnow().isoformat(),
            "agent": self.to_dict(),  # include symbolic metadata
            "trail": []  # trail starts here
        }

    def remix_insight(self, parent_insight: Dict, new_content: str, layer: str = "L3") -> Dict:
        """
        Remix an existing insight, transforming it with new content and symbolic state.

        Args:
            parent_insight (Dict): The insight to be remixed.
            new_content (str): The modified or evolved insight content.
            layer (str): The memory layer representing remix (default: L3).

        Returns:
            Dict: A new insight representing the remix with provenance and emotional logic.
        """
        return {
            "id": str(uuid.uuid4()),  # new ID for the remixed insight
            "content": new_content,
            "layer": layer,
            "emotion": self.emotion,
            "createdBy": self.glyph,
            "remixOf": parent_insight.get("id"),  # track provenance
            "parentEmotion": parent_insight.get("emotion"),  # symbolic feedback
            "timestamp": datetime.utcnow().isoformat(),
            "agent": self.to_dict(),
            "trail": parent_insight.get("trail", []) + [parent_insight.get("id")]
        }

    def to_dict(self) -> Dict:
        """
        Serialize the agent’s symbolic metadata for embedding in an insight.

        Returns:
            Dict: Serialized glyph, emotion, role, and goal.
        """
        return {
            "glyph": self.glyph,
            "emotion": self.emotion,
            "role": self.role,
            "goal": self.goal
        }
