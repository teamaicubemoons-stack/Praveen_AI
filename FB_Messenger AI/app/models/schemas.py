from pydantic import BaseModel
from typing import List, Optional

class WebhookEntry(BaseModel):
    id: str
    time: int
    messaging: Optional[List[dict]] = None

class WebhookRequest(BaseModel):
    object: str
    entry: List[WebhookEntry]

class AIResponse(BaseModel):
    intent: str
    response: str
    language: str
