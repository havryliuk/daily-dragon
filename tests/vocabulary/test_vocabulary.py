import json
from unittest.mock import patch, mock_open

from vocabulary.vocabulary import Vocabulary, Word

mock_vocabulary = {
    "word1": {
        "pronunciation": "pronunciation1",
        "translation": "translation1"
    },
    "word2": {
        "pronunciation": "pronunciation2",
        "translation": "translation2"
    }
}


def test_new_vocabulary():
    vocabulary = Vocabulary(1)
    assert vocabulary.vocabulary == {}


def test_save_word():
    mock_file_data = json.dumps(mock_vocabulary)

    with patch("builtins.open", mock_open(read_data=mock_file_data)):
        instance = Vocabulary("mock_file.json")
        word = Word("word3", "pronunciation3", "translation3")
        instance.save_word(word)

        mock_vocabulary["word3"] = {"pronunciation": "pronunciation3", "translation": "translation3"}
        assert instance.vocabulary == mock_vocabulary
        mock_vocabulary.pop("word3")


def test_save_word_already_exists():
    mock_file_data = json.dumps(mock_vocabulary)

    with patch("builtins.open", mock_open(read_data=mock_file_data)):
        instance = Vocabulary("mock_file.json")
        word = Word("word1", "pronunciation1", "translation1")
        try:
            instance.save_word(word)
        except ValueError as e:
            assert str(e) == "Word word1 already exists in vocabulary."
            assert instance.vocabulary == mock_vocabulary
        else:
            assert False


def test_get_words():
    mock_file_data = json.dumps(mock_vocabulary)

    with patch("builtins.open", mock_open(read_data=mock_file_data)):
        instance = Vocabulary("mock_file.json")
        assert instance.get_random_words(1)[0] in ["word1", "word2"]


def test_get_words_all():
    mock_file_data = json.dumps(mock_vocabulary)

    with patch("builtins.open", mock_open(read_data=mock_file_data)):
        instance = Vocabulary("mock_file.json")
        assert instance.get_random_words(3) == ["word1", "word2"]


def test_word_str():
    word = Word("word", "pronunciation", "translation")
    assert str(word) == "word (pronunciation) - translation"
