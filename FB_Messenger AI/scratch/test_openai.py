import sys
import os
import asyncio

# Add app directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.services.openai_service import openai_service

async def test_openai():
    print("🤖 Testing final response (Kya tum AI ho?)...")
    try:
        response = await openai_service.get_intent_and_response(
            "Kya tum AI ho ?"
        )
        print(f"💬 Response 1: {response.get('response')}")
        
        response2 = await openai_service.get_intent_and_response(
            "Mujhe ek pice shirt chahiye tha mil jayega kya ?"
        )
        print(f"💬 Response 2: {response2.get('response')}")
    except Exception as e:
        print(f"❌ Error occurred: {e}")

if __name__ == "__main__":
    asyncio.run(test_openai())
