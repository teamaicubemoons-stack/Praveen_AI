import requests
import json

# Your local FB Messenger server URL (running on port 8001)
URL = "http://127.0.0.1:8001/api/v1/webhook"

# Simulated Facebook Messenger Webhook Data
test_data = {
    "object": "page",
    "entry": [
        {
            "id": "900767499793934",
            "time": 1717390000,
            "messaging": [
                {
                    "sender": {"id": "987654321"}, # Fake FB User ID
                    "recipient": {"id": "900767499793934"},
                    "timestamp": 1717390000,
                    "message": {
                        "mid": "mid.12345",
                        "text": "Hello! Do you sell wholesale kurtas and sarees?"
                    }
                }
            ]
        }
    ]
}

def test_local_webhook():
    print(f"🚀 Sending test FB Messenger message to: {URL}")
    try:
        response = requests.post(URL, json=test_data)
        print(f"📡 Status Code: {response.status_code}")
        print(f"📄 Response: {response.json()}")
        print("\n✅ Test request sent! Check your Uvicorn terminal for Messenger AI logs.")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_local_webhook()
