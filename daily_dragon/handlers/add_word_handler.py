from telegram import Update
from telegram.ext import ConversationHandler, CommandHandler, MessageHandler, filters, ContextTypes

from daily_dragon.vocabulary.vocabulary import Word, Vocabulary

word, pronunciation, translation = range(3)

def add_word_handler():
    return ConversationHandler(
        entry_points=[CommandHandler('add_word', add_word)],
        states={
            word: [MessageHandler(filters.TEXT & ~filters.COMMAND, add_pronunciation)],
            pronunciation: [MessageHandler(filters.TEXT & ~filters.COMMAND, add_translation)],
            translation: [MessageHandler(filters.TEXT & ~filters.COMMAND, save_word)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )


async def add_word(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("Enter the word:")
    return word


async def add_pronunciation(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data['word'] = update.message.text
    await update.message.reply_text("Enter the pronunciation:")
    return pronunciation


async def add_translation(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data['pronunciation'] = update.message.text
    await update.message.reply_text("Enter the translation:")
    return translation


async def save_word(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data['translation'] = update.message.text
    word = Word(context.user_data['word'], context.user_data['pronunciation'], context.user_data['translation'])

    vocabulary = Vocabulary(update.effective_user.id)
    try:
        vocabulary.save_word(word)
        reply = f"Word saved: {word}"
    except ValueError:
        reply = f"Word {word.word} already exists in vocabulary."

    await update.message.reply_text(reply)
    return ConversationHandler.END


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("Word entry cancelled.")
    return ConversationHandler.END
