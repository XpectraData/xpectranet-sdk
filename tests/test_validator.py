import unittest
from validation.validator import ValidatorEngine

class TestValidatorEngine(unittest.TestCase):
    def setUp(self):
        self.policy_path = "circles/circle-policy.yaml"

        self.agent_validator = {"role": "validator"}
        self.agent_remixer = {"role": "remixer"}

        self.parent = {
            "id": "abc123",
            "layer": "L3",
            "emotion": "grief"
        }

    def test_layer_progression_valid(self):
        insight = {
            "layer": "L4",
            "emotion": "awe"
        }
        valid = ValidatorEngine.validate_insight(self.agent_validator, insight, self.parent, self.policy_path)
        self.assertTrue(valid)

    def test_fails_same_emotion(self):
        insight = {
            "layer": "L4",
            "emotion": "grief"
        }
        valid = ValidatorEngine.validate_insight(self.agent_validator, insight, self.parent, self.policy_path)
        self.assertFalse(valid)

    def test_fails_role_restriction(self):
        insight = {
            "layer": "L4",
            "emotion": "awe"
        }
        valid = ValidatorEngine.validate_insight(self.agent_remixer, insight, self.parent, self.policy_path)
        self.assertFalse(valid)

    def test_passes_canonization(self):
        insight = {
            "layer": "L7",
            "trail": ["a", "b"],
            "divergenceScore": 0.5
        }
        passed = ValidatorEngine.validate_canonization(self.agent_validator, insight, self.policy_path)
        self.assertTrue(passed)

    def test_fails_canonization_due_to_depth(self):
        insight = {
            "layer": "L7",
            "trail": ["a"],
            "divergenceScore": 0.5
        }
        passed = ValidatorEngine.validate_canonization(self.agent_validator, insight, self.policy_path)
        self.assertFalse(passed)

    def test_fails_canonization_due_to_role(self):
        insight = {
            "layer": "L7",
            "trail": ["a", "b"],
            "divergenceScore": 0.5
        }
        passed = ValidatorEngine.validate_canonization(self.agent_remixer, insight, self.policy_path)
        self.assertFalse(passed)

if __name__ == "__main__":
    unittest.main()
