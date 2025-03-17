import logging
import re

from telegram import Update
from telegram.ext import ConversationHandler, CommandHandler, ContextTypes, MessageHandler, filters

from openai_client.daily_dragon import DailyDragon
from handlers.constants import JAPANESE_USER_ID
from vocabulary.vocabulary import Vocabulary

WORDS_COUNT_FOR_PRACTICE = 10

translation = range(1)


def format_sentence_to_underline(message: str) -> str:
    return re.sub(r'(<|>)', lambda m: '<u>' if m.group(0) == '<' else '</u>', message)


def practice_handler():
    return ConversationHandler(
        entry_points=[CommandHandler('practice', start_practice)],
        states={
            translation: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_translations)]
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )


async def start_practice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    logging.info(f'User {user_id} ("{update.effective_user.username}") started practice')

    vocabulary = Vocabulary(user_id)
    words = vocabulary.get_random_words(WORDS_COUNT_FOR_PRACTICE)

    daily_dragon = DailyDragon()
    if user_id == JAPANESE_USER_ID:
        daily_dragon.set_language('Japanese')

    sentences = daily_dragon.get_sentences_for_practice(words)
    for item in sentences['sentences']:
        item['sentence'] = format_sentence_to_underline(item['sentence'])

    context.user_data['sentences'] = sentences['sentences']
    context.user_data['current_sentence'] = 0
    context.user_data['translations'] = {}

    await update.message.reply_text(
        f"Translate the following sentences. Pay attention to the underlined words.\n{sentences['sentences'][0]['sentence']}",
        parse_mode='HTML')
    return translation


async def get_translations(update: Update, context: ContextTypes.DEFAULT_TYPE):
    current_sentence = context.user_data['current_sentence']
    sentences = context.user_data['sentences']

    sentences[current_sentence]['translation'] = update.message.text
    current_sentence += 1

    if current_sentence < len(sentences):
        context.user_data['current_sentence'] = current_sentence
        await update.message.reply_text(f"{sentences[current_sentence]['sentence']}", parse_mode='HTML')
        return translation
    else:
        await update.message.reply_text("Generating results...")
        daily_dragon = DailyDragon()
        marked_translations = daily_dragon.mark_translations(sentences)

        average_mark = sum(int(item['mark']) for item in marked_translations) / len(marked_translations)
        message_text = f"""
Practice completed. Here are your translations:

{'\n'.join(f"{item['sentence']} -> {item['translation']}\nMark: {item['mark']}\nComment: {item['comment']}\n" for item in marked_translations)}
You have practiced the following words: {", ".join(item['word'] for item in sentences)}
Average accuracy: {average_mark:.2f}
        """

        await update.message.reply_text(message_text, parse_mode='HTML')

        logging.info(f"User {update.effective_user.id} completed practice.")
        return ConversationHandler.END


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Practice cancelled.")
    return ConversationHandler.END
