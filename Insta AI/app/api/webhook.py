from fastapi import APIRouter, Request, HTTPException, Query, BackgroundTasks
from fastapi.responses import PlainTextResponse
from app.core.config import settings
from app.services.meta_service import meta_service
from app.services.openai_service import openai_service
from app.services.memory_service import memory_service
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

async def process_ai_response(sender_id: str, message_text: str):
    """
    Background task to handle AI logic and send the reply.
    Now includes chat history for context.
    """
    try:
        # 1. Get previous chat history
        history = memory_service.get_history(sender_id, limit=6)
        
        # 2. Get AI intent and response using history
        ai_data = await openai_service.get_intent_and_response(message_text, chat_history=history)
        response_text = ai_data.get("response", "I'm sorry, I couldn't process that.")
        
        # 3. Send message via Meta API
        success = await meta_service.send_message(sender_id, response_text)
        
        if success:
            logger.info(f"✅ Response successfully sent to {sender_id}")
            # 4. Save both messages to memory for next time
            memory_service.add_message(sender_id, "user", message_text)
            memory_service.add_message(sender_id, "assistant", response_text)
        else:
            logger.error(f"❌ Failed to send response to {sender_id}")
            
    except Exception as e:
        logger.error(f"❌ Error in background processing: {e}")

@router.get("/webhook")
async def verify_webhook(
    hub_mode: str = Query(None, alias="hub.mode"),
    hub_challenge: str = Query(None, alias="hub.challenge"),
    hub_verify_token: str = Query(None, alias="hub.verify_token")
):
    """
    Webhook verification for Meta. 
    Meta sends a GET request to verify the endpoint.
    """
    if hub_mode == "subscribe" and hub_verify_token == settings.WEBHOOK_VERIFY_TOKEN:
        logger.info("✅ Webhook verified successfully!")
        return PlainTextResponse(content=hub_challenge)
    
    logger.warning("❌ Webhook verification failed.")
    raise HTTPException(status_code=403, detail="Verification token mismatch")

@router.post("/webhook")
async def handle_webhook(request: Request, background_tasks: BackgroundTasks):
    """
    Handles incoming messages from Instagram DMs.
    Supports: Instagram API (object=instagram) AND Messenger Platform (object=page).
    """
    data = await request.json()
    logger.info(f"📥 RAW Webhook: {data}")
    
    obj = data.get("object")
    logger.info(f"🔎 Object type: {obj}")
    
    if obj == "instagram":
        for entry in data.get("entry", []):
            messaging_list = entry.get("messaging", [])
            changes_list = entry.get("changes", [])
            logger.info(f"📋 Messaging events: {len(messaging_list)}, Changes: {len(changes_list)}")
            
            # ✅ Format 1: "messaging" array — Messenger Platform & older Instagram API
            for i, messaging_event in enumerate(messaging_list):
                sender_id = messaging_event.get("sender", {}).get("id")
                message_data = messaging_event.get("message", {})
                logger.info(f"📌 Event[{i}] sender={sender_id}, message_keys={list(message_data.keys())}")
                
                if message_data.get("is_echo"):
                    logger.info("⏭️ Skipping echo message.")
                    continue
                
                if message_data.get("text") and sender_id:
                    recipient_id = messaging_event.get("recipient", {}).get("id")
                    # Ignore messages meant for Facebook Page (only process Instagram Business Account)
                    if recipient_id and settings.INSTAGRAM_BUSINESS_ACCOUNT_ID and recipient_id != settings.INSTAGRAM_BUSINESS_ACCOUNT_ID:
                        logger.info(f"⏭️ Skipping non-Instagram message. recipient_id={recipient_id}")
                        continue

                    message_text = message_data["text"]
                    logger.info(f"📩 [{obj}/messaging] Received from {sender_id}: {message_text}")
                    background_tasks.add_task(process_ai_response, sender_id, message_text)
                else:
                    logger.info(f"⏭️ Skipped — no text or sender. sender={sender_id}, text={message_data.get('text')}")

            # ✅ Format 2: "changes" array — newer Instagram Graph API
            for change in changes_list:
                if change.get("field") == "messages":
                    value = change.get("value", {})
                    sender_id = value.get("sender", {}).get("id")
                    message_data = value.get("message", {})
                    logger.info(f"📌 [changes] sender={sender_id}, message_keys={list(message_data.keys())}")
                    
                    if message_data.get("is_echo"):
                        logger.info("⏭️ Skipping echo message.")
                        continue
                    
                    if message_data.get("text") and sender_id:
                        recipient_id = value.get("recipient", {}).get("id")
                        # Ignore messages meant for Facebook Page
                        if recipient_id and settings.INSTAGRAM_BUSINESS_ACCOUNT_ID and recipient_id != settings.INSTAGRAM_BUSINESS_ACCOUNT_ID:
                            logger.info(f"⏭️ Skipping non-Instagram message in changes. recipient_id={recipient_id}")
                            continue

                        message_text = message_data["text"]
                        logger.info(f"📩 [{obj}/changes] Received from {sender_id}: {message_text}")
                        background_tasks.add_task(process_ai_response, sender_id, message_text)
                    else:
                        logger.info(f"⏭️ Skipped — no text or sender. sender={sender_id}, text={message_data.get('text')}")
                        
    return {"status": "ok"}


