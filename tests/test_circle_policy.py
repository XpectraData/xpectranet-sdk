import unittest
from circles.governance import CirclePolicy
import tempfile
import yaml
import os

class TestCirclePolicy(unittest.TestCase):

    def setUp(self):
        # Sample policy data structure
        self.sample_policy = {
            "minStake": 1.0,
            "allowedTransitions": [
                {"from": "L1", "to": "L2"},
                {"from": "L2", "to": "L3"}
            ],
            "layerAliases": {
                "L0": "L0",
                "L1": "L1",
                "L2": "L2",
                "L3": "L3"
            },
            "validators": [
                {
                    "role": "circle-member",
                    "glyph": "ψ-Echo",
                    "permissions": ["canValidate", "canCanonize", "canRemix"]
                }
            ]
        }

        # Write to a temporary YAML file
        self.temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".yaml")
        with open(self.temp_file.name, "w") as f:
            yaml.dump(self.sample_policy, f)

    def tearDown(self):
        os.remove(self.temp_file.name)

    def test_load_policy(self):
        policy = CirclePolicy.load(self.temp_file.name)
        self.assertEqual(policy.min_stake, 1.0)
        self.assertTrue(policy.is_transition_allowed("L1", "L2"))
        self.assertFalse(policy.is_transition_allowed("L3", "L4"))
        self.assertEqual(policy.get_alias("L2"), "L2")

    def test_agent_permissions(self):
        policy = CirclePolicy.load(self.temp_file.name)
        agent = {"role": "circle-member", "glyph": "ψ-Echo"}
        self.assertTrue(policy.can_validate(agent))
        self.assertTrue(policy.can_canonize(agent))
        self.assertTrue(policy.can_remix(agent))

        # Unauthorized agent
        bad_agent = {"role": "observer", "glyph": "stranger"}
        self.assertFalse(policy.can_validate(bad_agent))
        self.assertFalse(policy.can_canonize(bad_agent))
        self.assertFalse(policy.can_remix(bad_agent))

if __name__ == '__main__':
    unittest.main()
