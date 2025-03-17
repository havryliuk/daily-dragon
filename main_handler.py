import json
import logging
import os
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder

from handlers.add_word_handler import add_word_handler
from handlers.error_handler import error_handler
from handlers.list_words_handler import list_words_handler
from handlers.practice_handler import practice_handler
from handlers.random_word_handler import random_word_handler

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "YOUR_TELEGRAM_TOKEN_HERE")

application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

application.add_handler(add_word_handler())
application.add_handler(list_words_handler())
application.add_handler(random_word_handler())
application.add_handler(practice_handler())
application.add_error_handler(error_handler)


def lambda_handler(event, context):
    logging.info(event)
    update_data = json.loads(event["body"])

    update = Update.de_json(update_data, application.bot)

    asyncio.run(application.process_update(update))

    return {
        "statusCode": 200,
        "body": json.dumps("OK")
    }
