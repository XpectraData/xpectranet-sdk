from circles.governance import CirclePolicy
from protocol.quorum import QuorumEngine

class ValidatorEngine:
    """
    ValidatorEngine wraps the governance policy logic to evaluate whether
    symbolic insights can be validated or canonized within a Circle.

    It loads CirclePolicy from a YAML file and applies rules consistently.
    """

    @staticmethod
    def validate_insight(agent: dict, insight: dict, parent_insight: dict, policy_path: str = None) -> bool:
        """
        Validate a new symbolic insight using the governance policy.

        Args:
            agent (dict): The agent attempting validation.
            insight (dict): The new insight to be evaluated.
            parent_insight (dict): The original insight it was remixed from.
            policy_path (str): Optional path to Circle policy YAML (fallback: env or default path).

        Returns:
            bool: True if insight passes policy validation; False otherwise.
        """
        policy = CirclePolicy.load(policy_path)
        return policy.validate(agent, insight, parent_insight)

    @staticmethod
    def validate_canonization(agent: dict, insight: dict, policy_path: str = None) -> bool:
        """
        Determine whether an insight qualifies for canonization.

        Args:
            agent (dict): The agent proposing the insight for canonization.
            insight (dict): The candidate insight.

        Returns:
            bool: True if the insight qualifies to be canonized.
        """
        policy = CirclePolicy.load(policy_path)
        return policy.canonize(agent, insight)

    @staticmethod
    def validate_by_quorum(votes: list, policy_path: str = None) -> bool:
        """
        Perform quorum-based validation across a group of agent votes.

        Args:
            votes (list): List of votes, each with {"affirm": bool, "stake": float}
            policy_path (str): Optional path to YAML for Circle quorum settings

        Returns:
            bool: True if the quorum requirements are satisfied
        """
        policy = CirclePolicy.load(policy_path)
        quorum_rules = policy.rules.get("quorum", {})

        vote_method = quorum_rules.get("voteMethod", "count")
        if vote_method == "stake-weighted":
            threshold = quorum_rules.get("requiredStakePercent", 0.51)
            return QuorumEngine.stake_weighted_vote(votes, threshold)
        else:
            required = quorum_rules.get("requiredValidators", 2)
            return QuorumEngine.has_quorum(votes, required)
