from circles.governance import CirclePolicy

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
        Evaluate whether a symbolic insight is ready for canonization.

        Args:
            agent (dict): The agent proposing the insight for canonization.
            insight (dict): The insight to be considered for elevation.

        Returns:
            bool: True if insight meets the canonization policy rules.
        """
        policy = CirclePolicy.load(policy_path)
        return policy.canonize(agent, insight)
