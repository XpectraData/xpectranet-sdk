import unittest
from protocol.staking import XPDTStaking

class TestXPDTStaking(unittest.TestCase):

    def test_meets_stake_requirement_true(self):
        agent = {"glyph": "ψ-Echo", "stake": 2.0}
        self.assertTrue(XPDTStaking.meets_stake_requirement(agent, 1.5))

    def test_meets_stake_requirement_false(self):
        agent = {"glyph": "ψ-Echo", "stake": 0.5}
        self.assertFalse(XPDTStaking.meets_stake_requirement(agent, 1.0))

    def test_distribute_reward_exact_split(self):
        validators = [
            {"glyph": "A"},
            {"glyph": "B"},
            {"glyph": "C"}
        ]
        split = [0.4, 0.4, 0.2]
        total = 10.0

        result = XPDTStaking.distribute_reward(total, validators, split)

        self.assertEqual(len(result), 3)
        self.assertEqual(result[0]["recipient"], "A")
        self.assertAlmostEqual(result[0]["amount"], 4.0)
        self.assertAlmostEqual(result[1]["amount"], 4.0)
        self.assertAlmostEqual(result[2]["amount"], 2.0)

    def test_distribute_reward_rounding(self):
        validators = [{"glyph": "X"}, {"glyph": "Y"}]
        split = [0.5, 0.5]
        total = 7.777
        result = XPDTStaking.distribute_reward(total, validators, split)
        self.assertEqual(result[0]["amount"], 3.8885)
        self.assertEqual(result[1]["amount"], 3.8885)

if __name__ == "__main__":
    unittest.main()
