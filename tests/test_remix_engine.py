import unittest
from remix.remix_engine import RemixEngine

# Minimal mock agent that uses the same remix_insight contract
class MockAgent:
    def __init__(self, glyph, remixMotivation):
        self.glyph = glyph
        self.remixMotivation = remixMotivation

    def remix_insight(self, parent, new_content, layer="L3"):
        return {
            "content": new_content,
            "remixOf": parent["id"],
            "trail": parent.get("trail", []) + [parent["id"]],
            "layer": layer,
            "createdBy": self.glyph,
            "remixMotivation": self.remixMotivation
        }

class TestRemixEngine(unittest.TestCase):
    def setUp(self):
        self.parent_insight = {
            "id": "abc123",
            "content": "The market appears stable.",
            "trail": []
        }

    def test_remix_with_diverge_motivation(self):
        agent = MockAgent(glyph="ψ-Echo", remixMotivation="diverge")
        result = RemixEngine.remix(agent, self.parent_insight)
        self.assertIn("divergenceScore", result)
        self.assertIn("What if we challenged this?", result["content"])
        self.assertEqual(result["remixOf"], "abc123")

    def test_remix_with_amplify_motivation(self):
        agent = MockAgent(glyph="ψ-Echo", remixMotivation="amplify")
        result = RemixEngine.remix(agent, self.parent_insight)
        self.assertIn("more important", result["content"])
        self.assertAlmostEqual(result["divergenceScore"] >= 0.0, True)

    def test_remix_with_harmonize_motivation(self):
        agent = MockAgent(glyph="ψ-Echo", remixMotivation="harmonize")
        result = RemixEngine.remix(agent, self.parent_insight)
        self.assertIn("aligns with broader patterns", result["content"])

if __name__ == "__main__":
    unittest.main()
