from pydantic import BaseModel
from typing import Dict, Optional



class FCMToken(BaseModel):
    fcm_token: str

class Notification(BaseModel):
    title: str
    body: str
    data: Optional[Dict[str, str]] = {}
    image_url: Optional[str] = None
    action_url: Optional[str] = None


