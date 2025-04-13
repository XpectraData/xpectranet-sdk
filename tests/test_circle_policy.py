import unittest
import os
from circles.governance import CirclePolicy

class TestCirclePolicy(unittest.TestCase):
    def setUp(self):
        # Set env to default policy
        os.environ["XKO_POLICY_PATH"] = "circles/circle-policy.yaml"
        self.policy = CirclePolicy.load()

        self.agent_validator = {"role": "validator"}
        self.agent_remixer = {"role": "remixer"}

        self.parent = {
            "id": "123",
            "layer": "L3",
            "emotion": "awe"
        }

    def test_layer_progression_passes(self):
        insight = {
            "layer": "L4",
            "emotion": "grief"
        }
        self.assertTrue(self.policy.validate(self.agent_validator, insight, self.parent))

    def test_same_emotion_fails(self):
        insight = {
            "layer": "L4",
            "emotion": "awe"
        }
        self.assertFalse(self.policy.validate(self.agent_validator, insight, self.parent))

    def test_invalid_role_cannot_validate(self):
        insight = {
            "layer": "L4",
            "emotion": "grief"
        }
        self.assertFalse(self.policy.validate(self.agent_remixer, insight, self.parent))

    def test_canonization_with_sufficient_score_and_depth(self):
        insight = {
            "layer": "L7",
            "divergenceScore": 0.4,
            "trail": ["a", "b", "c"]
        }
        self.assertTrue(self.policy.canonize(self.agent_validator, insight))

    def test_canonization_fails_if_role_not_allowed(self):
        insight = {
            "layer": "L7",
            "divergenceScore": 0.4,
            "trail": ["a", "b", "c"]
        }
        self.assertFalse(self.policy.canonize(self.agent_remixer, insight))

if __name__ == "__main__":
    unittest.main()
