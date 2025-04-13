import unittest
from validation.validator import ValidatorEngine

class TestValidatorQuorum(unittest.TestCase):
    def setUp(self):
        self.policy_path = "circles/circle-policy-quorum.yaml"

    def test_stake_weighted_pass(self):
        votes = [
            {"affirm": True, "stake": 1.5},
            {"affirm": True, "stake": 1.0},
            {"affirm": False, "stake": 0.5}
        ]
        passed = ValidatorEngine.validate_by_quorum(votes, self.policy_path)
        self.assertTrue(passed)

    def test_stake_weighted_fail(self):
        votes = [
            {"affirm": True, "stake": 0.5},
            {"affirm": False, "stake": 1.5},
            {"affirm": False, "stake": 1.0}
        ]
        passed = ValidatorEngine.validate_by_quorum(votes, self.policy_path)
        self.assertFalse(passed)

    def test_validator_count_pass(self):
        # Override method in policy YAML to count instead of stake
        local_path = "circles/circle-policy.yaml"  # assume default uses count
        votes = [
            {"affirm": True, "stake": 1.0},
            {"affirm": True, "stake": 2.0},
            {"affirm": False, "stake": 1.0}
        ]
        passed = ValidatorEngine.validate_by_quorum(votes, local_path)
        self.assertTrue(passed)

    def test_validator_count_fail(self):
        local_path = "circles/circle-policy.yaml"
        votes = [
            {"affirm": True, "stake": 1.0},
            {"affirm": False, "stake": 2.0},
            {"affirm": False, "stake": 1.0}
        ]
        passed = ValidatorEngine.validate_by_quorum(votes, local_path)
        self.assertFalse(passed)

if __name__ == "__main__":
    unittest.main()
