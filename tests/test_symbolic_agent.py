import unittest
from agents.symbolic_agent import SymbolicAgent

class TestSymbolicAgent(unittest.TestCase):
    def setUp(self):
        self.agent = SymbolicAgent(
            glyph="ψ-Echo",
            role="remixer",
            remixMotivation="diverge",
            goal="challenge assumptions"
        )

    def test_mint_insight_structure(self):
        insight = self.agent.mint_insight("The system appears stable.")
        self.assertIn("id", insight)
        self.assertIn("content", insight)
        self.assertEqual(insight["content"], "The system appears stable.")
        self.assertEqual(insight["layer"], "L1")
        self.assertEqual(insight["remixMotivation"], "diverge")
        self.assertEqual(insight["createdBy"], "ψ-Echo")

    def test_remix_insight_structure(self):
        parent = self.agent.mint_insight("The system appears stable.")
        remix = self.agent.remix_insight(parent, "But what if it's not?")
        self.assertIn("remixOf", remix)
        self.assertEqual(remix["layer"], "L3")
        self.assertEqual(remix["trail"], [parent["id"]])
        self.assertEqual(remix["remixOf"], parent["id"])
        self.assertEqual(remix["remixMotivation"], "diverge")

    def test_to_dict(self):
        profile = self.agent.to_dict()
        self.assertEqual(profile["glyph"], "ψ-Echo")
        self.assertEqual(profile["remixMotivation"], "diverge")
        self.assertEqual(profile["goal"], "challenge assumptions")

if __name__ == '__main__':
    unittest.main()
