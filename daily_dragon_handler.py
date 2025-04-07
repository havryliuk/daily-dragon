import asyncio
import base64
import json
import logging

import boto3
from telegram import Update
from telegram.ext import Application, CallbackContext

from daily_dragon.handlers.error_handler import error_handler
from daily_dragon.handlers.add_word_handler import add_word_handler
from daily_dragon.handlers.list_words_handler import list_words_handler
from daily_dragon.handlers.practice_handler import practice_handler
from daily_dragon.handlers.random_word_handler import random_word_handler


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

logger = logging.getLogger()
logger.setLevel(logging.INFO)

application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

application.add_handler(add_word_handler())
application.add_handler(list_words_handler())
application.add_handler(random_word_handler())
application.add_handler(practice_handler())

application.add_error_handler(error_handler)


def daily_dragon_handler(event, context):
    """Lambda function entry point for handling Telegram updates."""
    try:
        asyncio.run(application.initialize())

        body = json.loads(event.get("body", "{}"))

        update = Update.de_json(body, application.bot)
        logger.info(update)
        context = CallbackContext(application)

        asyncio.run(application.process_update(update))

        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Update processed successfully"})
        }

    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
