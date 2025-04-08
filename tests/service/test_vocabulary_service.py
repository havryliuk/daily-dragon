import pytest
from unittest.mock import MagicMock

from daily_dragon.service.vocabulary_service import VocabularyService


@pytest.fixture
def mock_repository():
    mock = MagicMock()
    mock.get_vocabulary.return_value = {
        "学习": {"adoption": 0, "date_added": "2025-04-08"},
        "大众": {"adoption": 1, "date_added": "2025-04-01"},
    }
    return mock


def test_add_word(mock_repository):
    service = VocabularyService(vocabulary_repository=mock_repository)
    service.add_word("测试")
    mock_repository.add_word.assert_called_once_with("测试")


def test_get_vocabulary(mock_repository):
    service = VocabularyService(vocabulary_repository=mock_repository)
    vocabulary = service.get_vocabulary()
    assert vocabulary == mock_repository.get_vocabulary.return_value
    mock_repository.get_vocabulary.assert_called_once()


def test_delete_word_exists(mock_repository):
    service = VocabularyService(vocabulary_repository=mock_repository)

    service.delete_word("大众")

    updated_vocab = {
        "学习": {"adoption": 0, "date_added": "2025-04-08"},
    }
    mock_repository.save_vocabulary.assert_called_once_with(updated_vocab)


def test_delete_word_not_exists(mock_repository):
    service = VocabularyService(vocabulary_repository=mock_repository)

    service.delete_word("不存在的词")

    mock_repository.save_vocab.assert_not_called()
