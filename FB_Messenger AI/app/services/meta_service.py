import httpx
import logging
from app.core.config import settings

logger = logging.getLogger(__name__)

class MetaService:
    def __init__(self):
        self.base_url = "https://graph.facebook.com/v19.0"
        self.access_token = settings.PAGE_ACCESS_TOKEN
        # Reuse a single AsyncClient instance to avoid connection overhead (keep-alive)
        self.client = httpx.AsyncClient(timeout=10.0)

    async def send_message(self, recipient_id: str, text: str):
        """Sends a text message to a user via Facebook Messenger API."""
        url = f"{self.base_url}/me/messages"
        payload = {
            "recipient": {"id": recipient_id},
            "message": {"text": text}
        }
        params = {"access_token": self.access_token}
        
        try:
            response = await self.client.post(url, json=payload, params=params)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            err_msg = getattr(e.response, "text", str(e)) if hasattr(e, "response") and e.response is not None else str(e)
            logger.error(f"Error sending message: {err_msg}")
            return None

meta_service = MetaService()
