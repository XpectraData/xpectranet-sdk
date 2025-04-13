import unittest
from unittest.mock import patch
from memory.compose_memory import ComposeMemory

class TestComposeMemory(unittest.TestCase):

    @patch("memory.compose_memory.requests.post")
    def test_store_success(self, mock_post):
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {
            "data": {
                "createInsight": {
                    "document": {
                        "id": "abc123"
                    }
                }
            }
        }

        test_insight = {"content": "This is a test."}
        result = ComposeMemory.store(test_insight)
        self.assertEqual(result, "abc123")

    @patch("memory.compose_memory.requests.post")
    def test_store_failure(self, mock_post):
        mock_post.return_value.status_code = 500
        mock_post.return_value.text = "Internal Error"
        result = ComposeMemory.store({"content": "fail case"})
        self.assertIsNone(result)

    @patch("memory.compose_memory.requests.post")
    def test_retrieve_success(self, mock_post):
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {
            "data": {
                "node": {
                    "content": {
                        "text": "Recovered insight"
                    }
                }
            }
        }

        result = ComposeMemory.retrieve("abc123")
        self.assertIn("text", result)
        self.assertEqual(result["text"], "Recovered insight")

    @patch("memory.compose_memory.requests.post")
    def test_retrieve_failure(self, mock_post):
        mock_post.return_value.status_code = 404
        mock_post.return_value.text = "Not found"
        result = ComposeMemory.retrieve("doesnotexist")
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()
