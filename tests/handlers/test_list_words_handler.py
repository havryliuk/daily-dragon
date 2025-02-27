from unittest.mock import MagicMock, patch, AsyncMock

import pytest
from telegram import Update, User
from telegram.ext import ContextTypes

from handlers.list_words_handler import list_words
from vocabulary.vocabulary import Vocabulary


@pytest.mark.asyncio
async def test_list_words():
    mock_user = MagicMock()
    mock_user.id = 123

    mock_update = MagicMock()
    mock_update.effective_user = mock_user
    mock_update.effective_chat.id = AsyncMock()

    mock_context = MagicMock()
    mock_context.bot.send_message = AsyncMock()

    mock_vocabulary = MagicMock(spec=Vocabulary)
    mock_vocabulary.get_all_words.return_value = {
        "位于": {
            "pronunciation": "wèiyú",
            "translation": "to be located",
            "added_on": 1738858114,
            "adoption": 0
        },
        "解释": {
            "pronunciation": "jiěshì",
            "translation": "explanation",
            "added_on": 1738858114,
            "adoption": 0
        }}

    with patch("handlers.list_words_handler.Vocabulary", return_value=mock_vocabulary):
        await list_words(mock_update, mock_context)
