from typing import Dict
import random

class RemixEngine:
    """
    A symbolic remix engine to transform insights using emotional logic and symbolic divergence.
    This module applies simple content-level transformation based on emotion and calculates a symbolic divergence score.
    """

    @staticmethod
    def remix(agent, parent_insight: Dict) -> Dict:
        """
        Remix the parent insight using the symbolic agent's emotional context.

        Args:
            agent (SymbolicAgent): The agent performing the remix.
            parent_insight (Dict): The insight to be remixed.

        Returns:
            Dict: A new remixed insight dictionary with altered content and updated metadata.
        """
        base_content = parent_insight.get("content", "")
        emotion = agent.emotion.lower()

        # Apply simple emotional transformation logic
        transformed_content = RemixEngine._apply_emotional_filter(base_content, emotion)

        # Generate a symbolic divergence score (0.0 to 1.0)
        divergence_score = RemixEngine._calculate_divergence(base_content, transformed_content)

        # Attach divergence metadata and return a remixed insight
        remixed = agent.remix_insight(parent_insight, new_content=transformed_content)
        remixed["divergenceScore"] = round(divergence_score, 3)
        return remixed

    @staticmethod
    def _apply_emotional_filter(content: str, emotion: str) -> str:
        """
        Modify content slightly based on the agent’s emotional state.

        Args:
            content (str): The original content.
            emotion (str): The emotional vector to apply.

        Returns:
            str: Transformed content.
        """
        if emotion == "grief":
            return f"{content} But something feels unresolved."
        elif emotion == "awe":
            return f"{content} There’s something deeper here."
        elif emotion == "doubt":
            return f"{content} Is this really true?"
        elif emotion == "hope":
            return f"{content} Yet, we still believe."
        else:
            return f"{content} [remixed with {emotion}]"

    @staticmethod
    def _calculate_divergence(original: str, remixed: str) -> float:
        """
        Naively estimate symbolic divergence between two strings using string length delta.

        Args:
            original (str): Original content.
            remixed (str): Remixed content.

        Returns:
            float: Divergence score between 0.0 (identical) and 1.0 (fully divergent).
        """
        len_orig = len(original)
        len_remix = len(remixed)
        return min(abs(len_remix - len_orig) / max(len_orig, 1), 1.0)
