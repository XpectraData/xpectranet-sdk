from typing import Dict, List

class XPDTStaking:
    """
    XPDTStaking provides utility functions to manage symbolic stake logic in the XpectraNet Protocol.

    This includes:
    - Verifying agent XPDT stake for validation or canonization
    - Simulating stake-weighted reward distribution to validators
    """

    @staticmethod
    def meets_stake_requirement(agent: Dict, min_required: float) -> bool:
        """
        Check if an agent has enough XPDT stake to participate in a ritual (e.g., validation).

        Args:
            agent (Dict): The agent profile (must include 'stake' field).
            min_required (float): The minimum XPDT required to qualify.

        Returns:
            bool: True if the agent meets or exceeds the requirement.
        """
        return agent.get("stake", 0.0) >= min_required

    @staticmethod
    def distribute_reward(total: float, validators: List[Dict], split: List[float]) -> List[Dict]:
        """
        Distribute a symbolic XPDT reward among validators according to configured split.

        Args:
            total (float): Total XPDT available to split.
            validators (List[Dict]): Agent objects (must include 'glyph' or 'role').
            split (List[float]): List of fractional percentages summing to 1.0 (e.g., [0.4, 0.4, 0.2])

        Returns:
            List[Dict]: Reward breakdown showing each validator's share.
        """
        result = []
        for i, agent in enumerate(validators):
            share = round(split[i] * total, 4)
            result.append({
                "recipient": agent.get("glyph") or agent.get("role"),
                "amount": share
            })
        return result
