from unittest.mock import patch, MagicMock, AsyncMock

import pytest
from telegram.ext import ConversationHandler

from handlers.add_word_handler import add_word_handler, add_word, add_pronunciation, add_translation, save_word, cancel


@patch("handlers.add_word_handler.ConversationHandler")
@patch("handlers.add_word_handler.CommandHandler")
@patch("handlers.add_word_handler.MessageHandler")
def test_add_word_handler(mock_message_handler, mock_command_handler, mock_conversation_handler):
    mock_message_handler.return_value = MagicMock()
    mock_command_handler.return_value = MagicMock()
    mock_conversation_handler.return_value = MagicMock()

    handler = add_word_handler()

    mock_conversation_handler.assert_called_once_with(
        entry_points=[mock_command_handler.return_value],
        states={
            0: [mock_message_handler.return_value],
            1: [mock_message_handler.return_value],
            2: [mock_message_handler.return_value],
        },
        fallbacks=[mock_command_handler.return_value],
    )
    assert handler == mock_conversation_handler.return_value


@pytest.mark.asyncio
@patch("handlers.add_word_handler.Update")
@patch("handlers.add_word_handler.ContextTypes.DEFAULT_TYPE")
async def test_add_word(mock_context, mock_update):
    mock_message = AsyncMock()
    mock_message.reply_text = AsyncMock()
    mock_update.message = mock_message

    result = await add_word(mock_update, mock_context)

    mock_message.reply_text.assert_called_once_with("Enter the word:")
    assert result == 0


@pytest.mark.asyncio
@patch("handlers.add_word_handler.Update")
@patch("handlers.add_word_handler.ContextTypes.DEFAULT_TYPE")
async def test_add_pronunciation(mock_context, mock_update):
    mock_message = AsyncMock()
    mock_message.text = "word"
    mock_message.reply_text = AsyncMock()
    mock_update.message = mock_message
    mock_context.user_data = {}

    result = await add_pronunciation(mock_update, mock_context)

    mock_message.reply_text.assert_called_once_with("Enter the pronunciation:")
    assert mock_context.user_data == {"word": "word"}
    assert result == 1


@pytest.mark.asyncio
@patch("handlers.add_word_handler.Update")
@patch("handlers.add_word_handler.ContextTypes.DEFAULT_TYPE")
async def test_add_translation(mock_context, mock_update):
    mock_message = AsyncMock()
    mock_message.reply_text = AsyncMock()
    mock_update.message = mock_message
    mock_update.message.text = "sample pronunciation"

    mock_context.user_data = {}

    result = await add_translation(mock_update, mock_context)

    mock_message.reply_text.assert_called_once_with("Enter the translation:")
    assert mock_context.user_data['pronunciation'] == "sample pronunciation"
    assert result == 2


@pytest.mark.asyncio
@patch("handlers.add_word_handler.Update")
@patch("handlers.add_word_handler.ContextTypes.DEFAULT_TYPE")
@patch("handlers.add_word_handler.Vocabulary")
@patch("handlers.add_word_handler.Word")
async def test_save_word_success(mock_word, mock_vocabulary, mock_context, mock_update):
    mock_message = AsyncMock()
    mock_message.reply_text = AsyncMock()
    mock_update.message = mock_message
    mock_update.message.text = "sample translation"

    mock_context.user_data = {
        'word': 'sample_word',
        'pronunciation': 'sample_pronunciation',
        'translation': 'sample_translation'
    }

    mock_word.return_value = MagicMock()
    mock_vocabulary_instance = MagicMock()
    mock_vocabulary.return_value = mock_vocabulary_instance

    mock_vocabulary_instance.save_word = AsyncMock()

    result = await save_word(mock_update, mock_context)

    mock_vocabulary_instance.save_word.assert_called_once_with(mock_word.return_value)
    mock_message.reply_text.assert_called_once()
    assert result == ConversationHandler.END


@pytest.mark.asyncio
@patch("handlers.add_word_handler.Update")
@patch("handlers.add_word_handler.ContextTypes.DEFAULT_TYPE")
@patch("handlers.add_word_handler.Vocabulary")
async def test_save_word_already_exists(mock_vocabulary, mock_context, mock_update):
    mock_message = AsyncMock()
    mock_message.reply_text = AsyncMock()
    mock_update.message = mock_message
    mock_update.message.text = "sample translation"

    mock_context.user_data = {
        'word': 'sample_word',
        'pronunciation': 'sample_pronunciation',
        'translation': 'sample_translation'
    }

    mock_vocabulary_instance = MagicMock()
    mock_vocabulary.return_value = mock_vocabulary_instance

    mock_vocabulary_instance.save_word.side_effect = ValueError

    result = await save_word(mock_update, mock_context)

    mock_message.reply_text.assert_called_once_with("Word sample_word already exists in vocabulary.")
    assert result == ConversationHandler.END


@pytest.mark.asyncio
@patch("handlers.add_word_handler.Update")
@patch("handlers.add_word_handler.ContextTypes.DEFAULT_TYPE")
async def test_cancel(mock_context, mock_update):
    mock_message = AsyncMock()
    mock_message.reply_text = AsyncMock()
    mock_update.message = mock_message

    result = await cancel(mock_update, mock_context)

    mock_message.reply_text.assert_called_once_with("Word entry cancelled.")
    assert result == ConversationHandler.END
