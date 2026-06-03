import asyncio
import os
import sys

# Add the project root to sys.path to allow importing app modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Mock settings if necessary or load .env
from dotenv import load_dotenv
load_dotenv()

from app.services.openai_service import openai_service

async def test_logic():
    test_cases = [
        "Tell me about your AI services.", # Pure English
        "What do you guys do at Cubemoons?", # Pure English
        "Hiring chal rahi hai kya?", # Hinglish
        "Mujhe website banwani hai.", # Hindi/Hinglish
        "Can I speak to someone about marketing?", # English
    ]

    for query in test_cases:
        print(f"\n--- Query: {query} ---")
        result = await openai_service.get_intent_and_response(query)
        print(f"Response: {result.get('response')}")

if __name__ == "__main__":
    asyncio.run(test_logic())
