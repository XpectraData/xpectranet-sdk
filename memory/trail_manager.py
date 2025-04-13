from typing import List, Optional

class TrailManager:
    """
    Manages the lineage of insights by maintaining a trail of parent IDs.
    """

    @staticmethod
    def append(trail: List[str], parent_id: Optional[str]) -> List[str]:
        """
        Appends the parent ID to the existing trail to maintain lineage.

        Args:
            trail (List[str]): The current trail of parent IDs.
            parent_id (Optional[str]): The ID of the parent insight.

        Returns:
            List[str]: The updated trail with the new parent ID appended.
        """
        if parent_id:
            return trail + [parent_id]
        return trail
