from typing import List, Dict

class QuorumEngine:
    """
    QuorumEngine simulates Circle-level validation consensus using votes and XPDT stake.

    Used to determine whether a set of validators can confirm (or reject) an insight
    according to configured CirclePolicy quorum rules.
    """

    @staticmethod
    def has_quorum(votes: List[Dict], required: int) -> bool:
        """
        Simple quorum check based on number of affirmative validators.

        Args:
            votes (List[Dict]): List of votes with "affirm": True/False
            required (int): Minimum number of affirmatives needed

        Returns:
            bool: True if quorum met
        """
        affirm_count = sum(1 for v in votes if v.get("affirm") is True)
        return affirm_count >= required

    @staticmethod
    def stake_weighted_vote(votes: List[Dict], threshold: float) -> bool:
        """
        Evaluate consensus based on stake-weighted quorum (e.g. 51% XPDT to affirm).

        Args:
            votes (List[Dict]): Each vote must include {"affirm": bool, "stake": float}
            threshold (float): Minimum percent (e.g., 0.51 for majority)

        Returns:
            bool: True if stake-weighted quorum passed
        """
        total_stake = sum(v.get("stake", 0.0) for v in votes)
        affirm_stake = sum(v.get("stake", 0.0) for v in votes if v.get("affirm") is True)

        if total_stake == 0:
            return False

        ratio = affirm_stake / total_stake
        return ratio >= threshold

    @staticmethod
    def summarize_votes(votes: List[Dict]) -> Dict:
        """
        Summarize voting outcome for logging or insight metadata.

        Args:
            votes (List[Dict]): Full vote record (affirm, stake)

        Returns:
            Dict: Summary (affirm count, dissent count, total stake, affirm stake)
        """
        affirm = [v for v in votes if v.get("affirm")]
        dissent = [v for v in votes if not v.get("affirm")]

        return {
            "affirmCount": len(affirm),
            "dissentCount": len(dissent),
            "totalStake": sum(v.get("stake", 0.0) for v in votes),
            "affirmStake": sum(v.get("stake", 0.0) for v in affirm)
        }
