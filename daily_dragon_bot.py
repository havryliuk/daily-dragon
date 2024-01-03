import logging
from dotenv import load_dotenv
import os

from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

from daily_dragon import DailyDragon

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

load_dotenv()
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
if TELEGRAM_TOKEN is None or TELEGRAM_TOKEN == '':
    raise ValueError('TELEGRAM_TOKEN not found in .env file')

daily_dragon = DailyDragon()


RAINY_BABE = 'rainy_babe'


async def daily_word(update: Update, context: ContextTypes.DEFAULT_TYPE):
    username = update.effective_user.username
    print(f'User {username} requested daily word')
    if username == RAINY_BABE:
        daily_dragon.set_language('Japanese')
    daily_word_response = daily_dragon.get_daily_word()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=daily_word_response)


if __name__ == '__main__':
    application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    
    start_handler = CommandHandler('dailyword', daily_word)
    application.add_handler(start_handler)
    
    application.run_polling()
