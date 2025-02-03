import logging

from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

from daily_dragon import DailyDragon

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

RAINY_BABE = 'rainy_babe'


async def random_word(update: Update, context: ContextTypes.DEFAULT_TYPE):
    username = update.effective_user.username
    logger.info(f'User {username} requested random word')

    daily_dragon = DailyDragon()
    if username == RAINY_BABE:
        daily_dragon.set_language('Japanese')
    daily_word_response = daily_dragon.get_daily_word()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=daily_word_response)


def random_word_handler():
    return CommandHandler('random', random_word)
