from unittest.mock import MagicMock, AsyncMock, patch

import pytest
from telegram import User, Message, Update
from telegram.ext import ContextTypes, ConversationHandler, MessageHandler

from handlers.practice_handler import format_sentence_to_underline, start_practice, WORDS_COUNT_FOR_PRACTICE, \
    get_translations, practice_handler
from openai_client.daily_dragon import DailyDragon
from vocabulary.vocabulary import Vocabulary


def test_format_sentence_to_underline():
    sentence = "This is a <sentence>."
    result = format_sentence_to_underline(sentence)
    assert result == "This is a <u>sentence</u>."


def test_practice_handler():
    translation = range(1)

    handler = practice_handler()
    assert isinstance(handler, ConversationHandler)
    assert translation in handler.states
    assert any(isinstance(state_handler, MessageHandler) for state_handler in handler.states[translation])


@pytest.mark.asyncio
async def test_start_practice():
    mock_user = MagicMock(spec=User)
    mock_user.id = 12345
    mock_user.username = "test_user"

    mock_message = AsyncMock(spec=Message)
    mock_update = MagicMock(spec=Update)
    mock_update.effective_user = mock_user
    mock_update.message = mock_message

    mock_context = MagicMock(spec=ContextTypes.DEFAULT_TYPE)
    mock_context.user_data = {}

    mock_vocabulary = MagicMock(spec=Vocabulary)
    mock_vocabulary.get_random_words.return_value = ["word1", "word2"]

    mock_daily_dragon = MagicMock(spec=DailyDragon)
    mock_daily_dragon.get_sentences_for_practice.return_value = {
        "sentences": [{"sentence": "This is a _test_ sentence."}]
    }

    with patch("handlers.practice_handler.Vocabulary", return_value=mock_vocabulary), \
            patch("handlers.practice_handler.DailyDragon", return_value=mock_daily_dragon):
        await start_practice(mock_update, mock_context)

        mock_vocabulary.get_random_words.assert_called_once_with(WORDS_COUNT_FOR_PRACTICE)
        mock_daily_dragon.get_sentences_for_practice.assert_called_once_with(["word1", "word2"])
        mock_message.reply_text.assert_called_once_with(
            "Translate the following sentences. Pay attention to the underlined words.\nThis is a _test_ sentence.",
            parse_mode='HTML'
        )

        assert "sentences" in mock_context.user_data
        assert mock_context.user_data["current_sentence"] == 0
        assert mock_context.user_data["translations"] == {}


@pytest.mark.asyncio
async def test_get_translations_continue():
    update = AsyncMock(spec=Update)
    update.message = AsyncMock(spec=Message)
    update.message.text = "Translated text"
    update.message.reply_text = AsyncMock()
    update.effective_user = MagicMock(spec=User)
    update.effective_user.id = 123

    context = MagicMock()
    context.user_data = {
        'current_sentence': 0,
        'sentences': [
            {'sentence': 'Hello', 'translation': ''},
            {'sentence': 'Goodbye', 'translation': ''}
        ]
    }

    result = await get_translations(update, context)

    assert context.user_data['current_sentence'] == 1
    update.message.reply_text.assert_called_once_with("Goodbye", parse_mode='HTML')
    assert result == range(0, 1)


@pytest.mark.asyncio
@patch("handlers.practice_handler.DailyDragon")  # Mock DailyDragon
async def test_get_translations_end(mock_daily_dragon):
    update = AsyncMock(spec=Update)
    update.message = AsyncMock(spec=Message)
    update.message.text = "Final translation"
    update.message.reply_text = AsyncMock()
    update.effective_user = MagicMock(spec=User)
    update.effective_user.id = 123

    context = MagicMock()
    context.user_data = {
        'current_sentence': 1,
        'sentences': [
            {'word': 'word1', 'sentence': 'Hello', 'translation': 'Hi'},
            {'word': 'word2', 'sentence': 'Goodbye', 'translation': ''}
        ]
    }

    mock_instance = mock_daily_dragon.return_value
    mock_instance.mark_translations.return_value = [
        {'word': 'word1', 'sentence': 'Hello', 'translation': 'Hi', 'mark': 5, 'comment': 'Good'},
        {'word': 'word2', 'sentence': 'Goodbye', 'translation': 'Final translation', 'mark': 4, 'comment': 'Decent'}
    ]

    result = await get_translations(update, context)

    update.message.reply_text.assert_any_call("Generating results...")
    update.message.reply_text.assert_called_with(
        """
Practice completed. Here are your translations:

Hello -> Hi
Mark: 5
Comment: Good

Goodbye -> Final translation
Mark: 4
Comment: Decent

You have practiced the following words: word1, word2
Average accuracy: 4.50
        """,
        parse_mode='HTML'
    )
    assert result == ConversationHandler.END
