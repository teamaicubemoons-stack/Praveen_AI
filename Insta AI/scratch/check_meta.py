import os
import re
import requests
from dotenv import load_dotenv

load_dotenv()

# We start by using the current PAGE_ACCESS_TOKEN (which is the System User Token)
SYSTEM_USER_TOKEN = os.getenv("PAGE_ACCESS_TOKEN")
PAGE_ID = "900767499793934"
ENV_FILE_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")

def exchange_and_subscribe():
    print("Step 1: Exchanging System User Token for Page Access Token...")
    url = f"https://graph.facebook.com/v19.0/{PAGE_ID}"
    params = {
        "fields": "access_token,name",
        "access_token": SYSTEM_USER_TOKEN
    }
    
    try:
        response = requests.get(url, params=params)
        data = response.json()
        
        if "access_token" not in data:
            print(f"❌ Failed to exchange token: {data}")
            return
            
        page_access_token = data["access_token"]
        print("✅ Received Page Access Token!")
        
        # Step 2: Update the .env file with the Page Access Token
        print("\nStep 2: Saving Page Access Token to .env...")
        with open(ENV_FILE_PATH, "r") as file:
            content = file.read()
            
        # Replace the PAGE_ACCESS_TOKEN value
        updated_content = re.sub(
            r"PAGE_ACCESS_TOKEN=.*",
            f"PAGE_ACCESS_TOKEN={page_access_token}",
            content
        )
        
        with open(ENV_FILE_PATH, "w") as file:
            file.write(updated_content)
            
        print("✅ Saved to .env!")
        
        # Step 3: Subscribe the page to the app
        print("\nStep 3: Subscribing Facebook Page to App Webhooks...")
        sub_url = f"https://graph.facebook.com/v19.0/{PAGE_ID}/subscribed_apps"
        sub_params = {
            "subscribed_fields": "messages,messaging_postbacks",
            "access_token": page_access_token
        }
        
        sub_resp = requests.post(sub_url, params=sub_params)
        print(f"Subscribe POST Status: {sub_resp.status_code}")
        print(f"Response: {sub_resp.json()}")
        
        # Step 4: Verify subscription status
        verify_resp = requests.get(sub_url, params={"access_token": page_access_token})
        print(f"\nVerify GET Status: {verify_resp.status_code}")
        print(f"Subscribed Apps List: {verify_resp.json()}")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    exchange_and_subscribe()
