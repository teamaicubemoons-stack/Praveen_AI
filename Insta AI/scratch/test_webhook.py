import requests
import json

# Your local server URL
URL = "http://127.0.0.1:8000/api/v1/webhook"

# Simulated Instagram Webhook Data
test_data = {
    "object": "instagram",
    "entry": [
        {
            "messaging": [
                {
                    "sender": {"id": "123456789"}, # Fake User ID
                    "message": {"text": "Hello! I want to know the price of your product."}
                }
            ]
        }
    ]
}

def test_local_webhook():
    print(f"🚀 Sending test message to: {URL}")
    try:
        response = requests.post(URL, json=test_data)
        print(f"📡 Status Code: {response.status_code}")
        print(f"📄 Response: {response.json()}")
        print("\n✅ Test request sent! Check your Uvicorn terminal for AI processing logs.")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_local_webhook()
