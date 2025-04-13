import unittest
from validation.validator import ValidatorEngine
from circles.governance import CirclePolicy
from protocol.quorum import QuorumEngine

class MockPolicy(CirclePolicy):
    def can_validate(self, agent):
        return agent.get("role") == "circle-member"

class MockQuorumEngine(QuorumEngine):
    def __init__(self, policy):
        self.policy = policy

    def evaluate(self, insight_id, votes):
        total_stake = sum(v["stake"] for v in votes)
        return total_stake >= 1.0

class TestValidatorEngine(unittest.TestCase):

    def setUp(self):
        self.policy = MockPolicy()
        self.insight_from = {"memoryPhase": "L1"}
        self.remix_insight = {"memoryPhase": "L2"}
        self.agent = {"role": "circle-member", "glyph": "ψ-Echo"}

        self.insight_canon = {"memoryPhase": "L7", "id": "insight:canon"}
        self.votes = [
            {"stake": 0.5, "glyph": "agent:one", "intent": "affirm"},
            {"stake": 0.6, "glyph": "agent:two", "intent": "affirm"}
        ]

    def test_validate_insight_success(self):
        result = ValidatorEngine.validate_insight(
            self.insight_from, self.remix_insight, self.agent, self.policy
        )
        self.assertTrue(result)

    def test_validate_insight_permission_error(self):
        self.agent["role"] = "observer"
        with self.assertRaises(PermissionError):
            ValidatorEngine.validate_insight(
                self.insight_from, self.remix_insight, self.agent, self.policy
            )

    def test_validate_canonization_success(self):
        result = ValidatorEngine.validate_canonization(
            self.insight_canon, self.votes, self.policy
        )
        self.assertTrue(result)

    def test_validate_canonization_layer_error(self):
        self.insight_canon["memoryPhase"] = "L4"
        with self.assertRaises(ValueError):
            ValidatorEngine.validate_canonization(
                self.insight_canon, self.votes, self.policy
            )

if __name__ == '__main__':
    unittest.main()
