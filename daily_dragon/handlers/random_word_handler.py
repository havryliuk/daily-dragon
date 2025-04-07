import logging

from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

from daily_dragon.openai_client.daily_dragon import DailyDragon
from daily_dragon.handlers.constants import JAPANESE_USER_ID

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)


async def random_word(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    logger.info(f'User {user_id} ("{update.effective_user.username}") requested random word')

    daily_dragon = DailyDragon()
    if user_id == JAPANESE_USER_ID:
        daily_dragon.set_language('Japanese')
    daily_word_response = daily_dragon.get_daily_word()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=daily_word_response)


def random_word_handler():
    return CommandHandler('random_word', random_word)
