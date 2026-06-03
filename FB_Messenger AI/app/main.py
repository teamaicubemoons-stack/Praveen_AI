import logging
import sys
from fastapi import FastAPI
from app.api import webhook
from app.core.config import settings
import uvicorn

# Configure Logging with a professional format
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-7s | %(name)s | %(message)s",
    datefmt="%H:%M:%S",
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger("app.main")

app = FastAPI(
    title="Messenger AI Automation",
    description="AI-powered FB Messenger DM automation backend",
    version="1.0.0"
)

# Include Routers
app.include_router(webhook.router, prefix="/api/v1", tags=["Messenger Webhook"])

@app.on_event("startup")
async def startup_event():
    """
    Runs on startup to verify all configurations and provide status logs.
    """
    logger.info("="*60)
    logger.info("🚀 INITIALIZING MESSENGER AI BACKEND SYSTEM")
    logger.info("="*60)
    
    # 1. Verify Meta / Messenger Config
    meta_status = "✅ LOADED" if all([settings.PAGE_ID, settings.PAGE_ACCESS_TOKEN]) else "❌ INCOMPLETE"
    logger.info(f"MODULE: Meta/Messenger Configuration -> {meta_status}")
    
    if settings.PAGE_ID:
        logger.info(f"   - Page ID: {settings.PAGE_ID}")
    else:
        logger.error("   - Page ID: MISSING (Check .env)")

    if settings.PAGE_ACCESS_TOKEN:
        masked = f"{settings.PAGE_ACCESS_TOKEN[:10]}...{settings.PAGE_ACCESS_TOKEN[-5:]}"
        logger.info(f"   - Access Token: {masked}")
    else:
        logger.error("   - Access Token: MISSING (Check .env)")

    logger.info(f"   - Verify Token: {settings.WEBHOOK_VERIFY_TOKEN}")

    # 2. Verify OpenAI Config
    openai_status = "✅ LOADED" if settings.OPENAI_API_KEY else "❌ MISSING"
    logger.info(f"MODULE: OpenAI Service Configuration -> {openai_status}")
    
    if settings.OPENAI_API_KEY:
        masked_key = f"{settings.OPENAI_API_KEY[:8]}...{settings.OPENAI_API_KEY[-4:]}"
        logger.info(f"   - API Key: {masked_key}")
        logger.info(f"   - AI Model: {settings.OPENAI_MODEL}")
    else:
        logger.error("   - API Key: MISSING (Check .env)")

    # 3. System Environment
    logger.info(f"SYSTEM: Environment Mode -> {'DEVELOPMENT (Debug On)' if settings.DEBUG else 'PRODUCTION'}")
    logger.info(f"SYSTEM: Serving on Port -> {settings.PORT}")
    
    logger.info("="*60)
    if meta_status == "✅ LOADED" and openai_status == "✅ LOADED":
        logger.info("✨ ALL SYSTEMS GREEN - BACKEND IS ACTIVE")
    else:
        logger.warning("⚠️ SYSTEM STARTED WITH ERRORS - PLEASE CHECK CONFIG")
    logger.info("="*60)

@app.get("/")
async def root():
    return {
        "message": "Messenger AI Backend is running",
        "docs": "/docs",
        "status": "healthy"
    }

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=settings.PORT, reload=settings.DEBUG)
