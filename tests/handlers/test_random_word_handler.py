from unittest.mock import AsyncMock, patch

import pytest

from daily_dragon.handlers import random_word


@pytest.mark.asyncio
@patch("handlers.random_word_handler.DailyDragon")
async def test_random_word_handler(mock_daily_dragon):
    mock_update = AsyncMock()
    mock_context = AsyncMock()
    mock_context.bot.send_message = AsyncMock()
    mock_update.effective_user.id = 391819710
    mock_update.effective_chat.id = 12345

    mock_instance = mock_daily_dragon.return_value
    mock_instance.get_daily_word.return_value = "Random Word"

    await random_word(mock_update, mock_context)

    mock_daily_dragon.assert_called_once()
    mock_instance.get_daily_word.assert_called_once()
    mock_context.bot.send_message.assert_called_once_with(chat_id=12345, text="Random Word")
