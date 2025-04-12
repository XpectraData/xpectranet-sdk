from typing import Dict
import random

class RemixEngine:
    """
    A symbolic remix engine that transforms insights using motivation or emotion.
    This component sits between the parent insight and the remixer agent, applying
    meaningful symbolic transformations and scoring divergence.

    Used by agent workflows to generate evolved insights while preserving lineage.
    """

    @staticmethod
    def remix(agent, parent_insight: Dict) -> Dict:
        """
        Apply symbolic transformation logic to the given insight, based on the agent's motivation.

        Args:
            agent: An instance of SymbolicAgent or similar agent implementing `remix_insight()`.
            parent_insight (Dict): The insight to be remixed.

        Returns:
            Dict: The remixed insight with modified content and symbolic metadata.
        """
        original = parent_insight.get("content", "")
        motivation = agent.remixMotivation or "explore"

        # Generate new content based on symbolic transformation
        new_content = RemixEngine._apply_motivation_filter(original, motivation)

        # Score symbolic divergence (how different it is from the original)
        divergence_score = RemixEngine._calculate_divergence(original, new_content)

        # Call agent's remix logic and attach the divergence
        remixed = agent.remix_insight(parent_insight, new_content)
        remixed["divergenceScore"] = round(divergence_score, 3)
        return remixed

    @staticmethod
    def _apply_motivation_filter(content: str, motivation: str) -> str:
        """
        Transform insight content based on symbolic motivation intent.

        Args:
            content (str): The original content to transform.
            motivation (str): The symbolic intent (e.g., 'diverge', 'amplify', 'harmonize').

        Returns:
            str: Transformed insight content.
        """
        if motivation == "diverge":
            return f"{content} What if we challenged this?"
        elif motivation == "amplify":
            return f"{content} This is more important than it seems."
        elif motivation == "harmonize":
            return f"{content} This aligns with broader patterns we’ve seen."
        elif motivation == "invert":
            return f"Let’s reverse this: {content[::-1]}"
        else:
            return f"{content} [remixed with motivation: {motivation}]"

    @staticmethod
    def _calculate_divergence(original: str, remixed: str) -> float:
        """
        Estimate symbolic divergence using content length delta as a simple heuristic.

        Args:
            original (str): Original insight content.
            remixed (str): Remixed version.

        Returns:
            float: A value from 0.0 (identical) to 1.0 (very different).
        """
        len_orig = len(original)
        len_remix = len(remixed)
        return min(abs(len_remix - len_orig) / max(len_orig, 1), 1.0)
