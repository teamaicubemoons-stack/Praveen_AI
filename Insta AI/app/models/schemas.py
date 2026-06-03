from pydantic import BaseModel, Field
from typing import List, Optional, Any

class WebhookEntry(BaseModel):
    id: str
    time: int
    messaging: Optional[List[dict]] = None
    changes: Optional[List[dict]] = None

class WebhookRequest(BaseModel):
    object: str
    entry: List[WebhookEntry]

class IntentResponse(BaseModel):
    intent: str
    confidence: float
    entities: dict = {}

class AIResponse(BaseModel):
    text: str
    language: str
