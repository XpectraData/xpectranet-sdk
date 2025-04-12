from abc import ABC, abstractmethod
from typing import Dict

class BaseAgent(ABC):
    """
    Abstract base class for symbolic cognition agents in the XpectraNet SDK.

    This class defines the core interface for any agent that interacts with symbolic memory —
    whether minting new insights, remixing existing ones, or serializing their identity.

    All concrete agent classes (e.g., SymbolicAgent, ValidatorAgent) must implement the following methods:
      - mint_insight
      - remix_insight
      - to_dict
    """

    @abstractmethod
    def mint_insight(self, content: str, layer: str = "L1") -> Dict:
        """
        Mint a new symbolic insight from scratch.

        Args:
            content (str): The raw content of the new insight.
            layer (str): The cognitive layer this insight originates from (default is 'L1').

        Returns:
            Dict: A structured insight object containing identity, metadata, and content.
        """
        pass

    @abstractmethod
    def remix_insight(self, parent_insight: Dict, new_content: str, layer: str = "L3") -> Dict:
        """
        Remix an existing insight based on its symbolic structure and motivation.

        Args:
            parent_insight (Dict): The insight being transformed.
            new_content (str): The modified or evolved content to output.
            layer (str): The symbolic layer this remix occupies (default is 'L3').

        Returns:
            Dict: A new insight with remix lineage and updated content.
        """
        pass

    @abstractmethod
    def to_dict(self) -> Dict:
        """
        Serialize the agent's symbolic identity and role metadata.

        Returns:
            Dict: A dictionary representation of the agent.
        """
        pass
