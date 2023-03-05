from requests.structures import CaseInsensitiveDict
import requests


def randint():
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"

    payload = """
    {
        "jsonrpc": "2.0",
        "method": "generateIntegers",
        "id": "1",
        "params": {
            "apiKey": "3b39990c-48ad-49fc-bbbf-a7b4a73d9cd4",
            "n": 1,
            "min": 0,
            "max": 1e9
        }
    }
    """

    response = requests.post("https://api.random.org/json-rpc/4/invoke", headers=headers, data=payload)
    return response.json()["result"]["random"]["data"][0]
