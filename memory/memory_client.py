from typing import Dict, List

class MemoryClient:
    """
    Handles storage and retrieval of insights in memory.
    """

    _insights: List[Dict] = []

    @classmethod
    def store_insight(cls, insight: Dict) -> None:
        """
        Stores a new insight in memory.

        Args:
            insight (Dict): The insight to store.
        """
        cls._insights.append(insight)

    @classmethod
    def get_insights(cls) -> List[Dict]:
        """
        Retrieves all stored insights.

        Returns:
            List[Dict]: A list of all stored insights.
        """
        return cls._insights

    @classmethod
    def clear_insights(cls) -> None:
        """
        Clears all stored insights.
        """
        cls._insights.clear()
