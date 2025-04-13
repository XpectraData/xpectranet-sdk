"""
TrailManager — Handles symbolic memory trail construction using XKO layer aliasing.

This class provides tools for:
- Layer alias resolution (L0–L9 → L0–L6)
- Building remix trails
- Appending to trails
- Producing symbolic summaries

All methods are stateless and can be used as utilities in agent logic or validator engines.
"""

from typing import List, Optional

class TrailManager:
    # Static alias map for converting full symbolic layer names to simplified 7-layer model
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

    @staticmethod
    def get_layer_alias(layer: str) -> str:
        """
        Convert a full symbolic layer (e.g., L4) into a simplified operational alias (e.g., L3).
        """
        return TrailManager.LAYER_ALIAS_MAP.get(layer, layer)

    @staticmethod
    def build_trail(remix_of: dict, current_insight_id: str) -> List[str]:
        """
        Construct a trail from the remix parent and append the current insight ID.

        Parameters:
            remix_of (dict): Parent insight dictionary containing optional 'trail'
            current_insight_id (str): ID of the new insight node

        Returns:
            list of str: Updated symbolic trail
        """
        parent_trail = remix_of.get("trail", [])
        return parent_trail + [current_insight_id]

    @staticmethod
    def append_to_trail(trail: Optional[List[str]], new_node_id: str) -> List[str]:
        """
        Append a new node ID to an existing trail, creating a new trail if none exists.

        Parameters:
            trail (list of str): Existing trail list
            new_node_id (str): New node to append

        Returns:
            list of str: Extended trail
        """
        if not trail:
            return [new_node_id]
        return trail + [new_node_id]

    @staticmethod
    def summarize_trail(trail_list: List[str]) -> str:
        """
        Create a symbolic summary of a trail using '→' notation.

        Parameters:
            trail_list (list of str): List of insight IDs or keys

        Returns:
            str: Symbolic summary string
        """
        return " → ".join(trail_list)
