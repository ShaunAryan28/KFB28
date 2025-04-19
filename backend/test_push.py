# test_push.py

from fcm_service import send_notification_to_all

# Sample test payload
title = "🚀 Test Notification"
body = "This is a manual test from test_push.py"
data = {"type": "test", "custom_id": "12345"}
image_url = ""  # optional, can be left empty or set to a public image URL
action_url = "https://example.com"  # optional

send_notification_to_all(title, body, data, image_url, action_url)
