import firebase_admin
from firebase_admin import messaging, credentials
from config import FIREBASE_CRED_PATH
from storage import get_all_tokens

# Initialize Firebase Admin SDK
cred = credentials.Certificate(FIREBASE_CRED_PATH)
firebase_admin.initialize_app(cred)

def send_notification_to_all(title, body, data, image_url, action_url):
    tokens = get_all_tokens()
    print("📱 Tokens found:", tokens)
    if not tokens:
        print("⚠️ No tokens found. Skipping push.")
        return

    for token in tokens:
        try:
            message = messaging.Message(
                token=token,
                notification=messaging.Notification(
                    title=title,
                    body=body,
                    image=image_url
                ),
                data={**data, "action_url": action_url} if data else {"action_url": action_url},
            )
            response = messaging.send(message)
            print(f"✅ Sent to {token}: {response}")
        except Exception as e:
            print(f"❌ Error sending to {token}: {e}")
