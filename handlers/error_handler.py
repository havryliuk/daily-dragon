import logging

from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler


async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logging.error(msg="Exception while handling an update:", exc_info=context.error)

    await update.message.reply_text('很抱歉，发生了意外错误……')
    return ConversationHandler.END
