import logging

from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

from daily_dragon.vocabulary.vocabulary import Vocabulary

WORDS_TO_RETURN = 10


async def list_words(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    vocabulary = Vocabulary(user_id)
    all_words = vocabulary.get_all_words()
    words_last_added = sorted(all_words.items(), key=lambda x: x[1]['added_on'], reverse=True)[:WORDS_TO_RETURN]

    response = "Last words added:\n" + ", ".join(
        [f"{word[0]}" for word in words_last_added]) + "\nTotal words in vocabulary: " + str(len(all_words))
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)
    logging.info(f"User {user_id} requested list of words")


def list_words_handler():
    return CommandHandler("list_words", list_words)
