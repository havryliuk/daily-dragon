from dotenv import load_dotenv
import os

from telegram.ext import ApplicationBuilder

from handlers.add_word_handler import add_word_handler
from handlers.error_handler import error_handler
from handlers.practice_handler import practice_handler
from handlers.random_word_handler import random_word_handler

load_dotenv()
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
if TELEGRAM_TOKEN is None or TELEGRAM_TOKEN == '':
    raise ValueError('TELEGRAM_TOKEN not found in .env file')

if __name__ == '__main__':
    application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    application.add_handler(random_word_handler())
    application.add_handler(add_word_handler())
    application.add_handler(practice_handler())

    application.add_error_handler(error_handler)

    application.run_polling()
