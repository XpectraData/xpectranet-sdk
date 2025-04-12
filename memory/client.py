import requests

CERAMIC_URL = "https://your-ceramic-node-url"

def write_insight(insight):
    mutation = '''
    mutation CreateInsight($i: CreateInsightInput!) {
      createInsight(input: $i) {
        document { id }
      }
    }
    '''
    payload = {
        "query": mutation,
        "variables": {"i": insight}
    }
    response = requests.post(CERAMIC_URL, json=payload)
    return response.json()
