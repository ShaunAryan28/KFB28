from fastapi import APIRouter, Request
from pydantic import BaseModel
from storage import save_token

router = APIRouter()

class TokenData(BaseModel):
    fcm_token: str

@router.post("/devices/register")
async def register_device(token_data: TokenData):
    save_token(token_data.fcm_token)
    return {"message": "Device registered"}
