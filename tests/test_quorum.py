import unittest
from protocol.quorum import QuorumEngine

class TestQuorumEngine(unittest.TestCase):

    def test_simple_quorum_pass(self):
        votes = [{"affirm": True}, {"affirm": True}, {"affirm": False}]
        self.assertTrue(QuorumEngine.has_quorum(votes, required=2))

    def test_simple_quorum_fail(self):
        votes = [{"affirm": True}, {"affirm": False}, {"affirm": False}]
        self.assertFalse(QuorumEngine.has_quorum(votes, required=2))

    def test_stake_weighted_pass(self):
        votes = [
            {"affirm": True, "stake": 1.5},
            {"affirm": False, "stake": 1.0},
            {"affirm": True, "stake": 2.0}
        ]
        self.assertTrue(QuorumEngine.stake_weighted_vote(votes, threshold=0.51))

    def test_stake_weighted_fail(self):
        votes = [
            {"affirm": True, "stake": 1.0},
            {"affirm": False, "stake": 2.0}
        ]
        self.assertFalse(QuorumEngine.stake_weighted_vote(votes, threshold=0.6))

    def test_vote_summary(self):
        votes = [
            {"affirm": True, "stake": 1.0},
            {"affirm": False, "stake": 2.0},
            {"affirm": True, "stake": 0.5}
        ]
        summary = QuorumEngine.summarize_votes(votes)
        self.assertEqual(summary["affirmCount"], 2)
        self.assertEqual(summary["dissentCount"], 1)
        self.assertAlmostEqual(summary["totalStake"], 3.5)
        self.assertAlmostEqual(summary["affirmStake"], 1.5)

if __name__ == "__main__":
    unittest.main()
