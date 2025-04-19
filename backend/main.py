from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from storage import save_token
from models import FCMToken, Notification
from publisher import publish_message
from consumer import start_consumer

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TokenRequest(BaseModel):
    fcm_token: str

@app.on_event("startup")
def startup_event():
    print("🔁 Starting consumer once on FastAPI startup")
    start_consumer()

@app.post("/devices/register")
async def register_device(req: TokenRequest):
    print("📩 Received token:", req.fcm_token)
    save_token(req.fcm_token)
    return {"message": "Device registered"}

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI 🚀"}

@app.post("/notifications/publish")
def publish_notification(notification: Notification):
    publish_message(notification.dict())
    return {"message": "Notification published"}
