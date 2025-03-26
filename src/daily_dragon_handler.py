import base64
import json

import boto3
import requests


def get_secret(secret_name: str) -> dict:
    region_name = "us-east-1"

    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    get_secret_value_response = client.get_secret_value(
        SecretId=secret_name
    )

    if 'SecretString' in get_secret_value_response:
        secret = get_secret_value_response['SecretString']
    else:
        secret = base64.b64decode(get_secret_value_response['SecretBinary'])

    secret_dict = json.loads(secret)
    return secret_dict


TELEGRAM_BOT_TOKEN = get_secret("DailyDragonTelegramToken")["TELEGRAM_BOT_TOKEN"]
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
