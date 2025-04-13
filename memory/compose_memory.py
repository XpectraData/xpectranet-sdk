import requests
from typing import Dict, Optional

# URL of the Ceramic ComposeDB node
CERAMIC_URL = "https://your-ceramic-node-url/graphql"  # Replace with your actual Ceramic GraphQL endpoint

class ComposeMemory:
    """
    ComposeMemory provides a bridge between XpectraNet's symbolic memory system
    and the decentralized ComposeDB/Ceramic infrastructure.

    This module enables reading and writing symbolic insights to a verifiable,
    persistent memory layer using GraphQL.
    """

    @staticmethod
    def store(insight: Dict) -> Optional[str]:
        """
        Store a symbolic insight on ComposeDB via a GraphQL mutation.

        Args:
            insight (Dict): The full structured insight object (content, layer, trail, etc.)

        Returns:
            Optional[str]: The ComposeDB document ID, or None if storage fails.
        """
        mutation = """
        mutation CreateInsight($i: CreateInsightInput!) {
            createInsight(input: $i) {
                document { id }
            }
        }
        """
        payload = {
            "query": mutation,
            "variables": {"i": {"content": insight}}
        }

        try:
            response = requests.post(CERAMIC_URL, json=payload)
            if response.status_code == 200:
                return response.json()["data"]["createInsight"]["document"]["id"]
            else:
                print("❌ ComposeDB storage failed:", response.text)
                return None
        except Exception as e:
            print("🚨 ComposeDB error:", str(e))
            return None

    @staticmethod
    def retrieve(insight_id: str) -> Optional[Dict]:
        """
        Retrieve an insight from ComposeDB using its ID.

        Args:
            insight_id (str): The ID of the document to fetch.

        Returns:
            Optional[Dict]: The insight's content, or None if retrieval fails.
        """
        query = """
        query GetInsight($id: ID!) {
            node(id: $id) {
                ... on Insight {
                    id
                    content
                }
            }
        }
        """
        payload = {
            "query": query,
            "variables": {"id": insight_id}
        }

        try:
            response = requests.post(CERAMIC_URL, json=payload)
            if response.status_code == 200:
                return response.json()["data"]["node"]["content"]
            else:
                print("❌ ComposeDB retrieval failed:", response.text)
                return None
        except Exception as e:
            print("🚨 ComposeDB error:", str(e))
            return None
