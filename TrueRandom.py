from requests.structures import CaseInsensitiveDict
import requests
import json
import os


def randint():
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"

    payload = {
        "jsonrpc": "2.0",
        "method": "generateIntegers",
        "id": "1",
        "params": {
            "apiKey": os.getenv("API_KEY"),
            "n": 1,
            "min": 0,
            "max": 1e9
        }
    }

    response = requests.post("https://api.random.org/json-rpc/4/invoke", headers=headers, data=json.dumps(payload))
    return response.json()["result"]["random"]["data"][0]
