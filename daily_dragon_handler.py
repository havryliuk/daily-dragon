import json
import requests

TELEGRAM_BOT_TOKEN = "6670842815:AAE-ro85Z-L0y77YIvaiH9WKZSDXguDcQ8M"
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

def daily_dragon_handler(event, context):
    try:
        body = json.loads(event.get("body", "{}"))

        chat_id = body["message"]["chat"]["id"]
        username = body["message"]["from"].get("username", "")
        user_id = body["message"]["from"]["id"]
        user_message = body["message"].get("text", "")

        bot_response = f"User '{username}' (user ID: {user_id}) wrote: {user_message}"

        response = requests.post(TELEGRAM_API_URL, json={
            "chat_id": chat_id,
            "text": bot_response
        })

        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Message sent", "response": response.json()})
        }

    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
