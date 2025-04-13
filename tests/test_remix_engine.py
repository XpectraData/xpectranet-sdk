import unittest
from remix.remix_engine import RemixEngine

# Mock memory and trail managers
class MockTrailManager:
    @staticmethod
    def append(trail, parent_id):
        return trail + [parent_id] if parent_id else trail

class MockMemoryClient:
    stored = []

    @classmethod
    def store_insight(cls, insight):
        cls.stored.append(insight)

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

class TestRemixEngineIntegration(unittest.TestCase):
    def setUp(self):
        # Patch dependencies
        RemixEngine._calculate_divergence = lambda o, t: 0.7
        RemixEngine._apply_motivation_filter = lambda c, m: f"{c} — remixed with {m}"
        RemixEngine.TrailManager = MockTrailManager
        RemixEngine.MemoryClient = MockMemoryClient

        self.agent = MockAgent("ψ-Echo", "diverge")
        self.parent_insight = {
            "id": "abc123",
            "content": "Truth must be questioned.",
            "trail": ["origin"]
        }

    def test_remix_engine_generates_trail_and_stores(self):
        insight = RemixEngine.remix(self.agent, self.parent_insight)
        self.assertIn("remixOf", insight)
        self.assertIn("divergenceScore", insight)
        self.assertTrue(len(insight["trail"]) > 1)
        self.assertIn(insight, RemixEngine.MemoryClient.stored)
        
if __name__ == "__main__":
    unittest.main()
