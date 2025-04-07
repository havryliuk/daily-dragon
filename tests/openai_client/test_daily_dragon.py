from unittest.mock import patch, MagicMock

from daily_dragon.openai_client import DailyDragon

@patch('openai_client.daily_dragon.OpenAI')
def test_init(openai_mock):
    openai_mock.return_value = 'openai_client'

    daily_dragon = DailyDragon()
    assert daily_dragon.openai_client == 'openai_client'
    assert daily_dragon.language == 'Chinese'


@patch('openai_client.daily_dragon.prompts')
@patch('openai_client.daily_dragon.OpenAI')
def test_get_daily_word(mock_openai_class, prompts_mock):
    prompts_mock.get_daily_word_prompt.return_value = '{language} prompt'

    mock_openai_instance = MagicMock()
    mock_openai_class.return_value = mock_openai_instance

    completion = MagicMock()
    completion.choices[0].message.content = 'word'
    mock_openai_instance.chat.completions.create.return_value = completion

    dragon = DailyDragon()

    result = dragon.get_daily_word()

    prompts_mock.get_daily_word_prompt.assert_called_once()
    mock_openai_class.assert_called_once()
    mock_openai_instance.chat.completions.create.assert_called_once_with(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a teacher of Chinese."},
            {"role": "user", "content": "Chinese prompt"}
        ]
    )
    assert result == 'word'

@patch('openai_client.daily_dragon.prompts')
@patch('openai_client.daily_dragon.OpenAI')
def test_get_sentences_for_practice(mock_openai_class, prompts_mock):
    prompts_mock.get_sentences_for_practice_prompt.return_value = '{language} and {words}'

    mock_openai_instance = MagicMock()
    mock_openai_class.return_value = mock_openai_instance

    completion = MagicMock()
    completion.choices[0].message.content = '{"sentences":[{"sentence":"s","word":"w"}]}'
    mock_openai_instance.chat.completions.create.return_value = completion

    daily_dragon = DailyDragon()
    result = daily_dragon.get_sentences_for_practice(['word1', 'word2'])

    daily_dragon.openai_client.chat.completions.create.assert_called_once_with(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a teacher of Chinese."},
            {"role": "user", "content": "Chinese and ['word1', 'word2']"}
        ]
    )
    assert result == {'sentences': [{'sentence': 's', 'word': 'w'}]}
