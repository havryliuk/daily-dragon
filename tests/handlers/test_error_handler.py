from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from telegram import Update, Message, User
from telegram.ext import ConversationHandler

from daily_dragon.handlers import error_handler


@pytest.mark.asyncio
async def test_error_handler():
    update = AsyncMock(spec=Update)
    update.message = AsyncMock(spec=Message)
    update.message.reply_text = AsyncMock()
    update.effective_user = MagicMock(spec=User)
    update.effective_user.id = 123

    context = MagicMock()
    context.error = Exception("Test exception")

    with patch("logging.error") as mock_logging:
        result = await error_handler(update, context)

        mock_logging.assert_called_once_with(msg="Exception while handling an update:", exc_info=context.error)
        update.message.reply_text.assert_called_once_with("很抱歉，发生了意外错误……")
        assert result == ConversationHandler.END