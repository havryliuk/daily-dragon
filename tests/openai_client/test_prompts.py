from openai_client.prompts import get_daily_word_prompt


def test_get_daily_prompt():
    prompt = get_daily_word_prompt()
    assert prompt == ('Provide me one random new {language} word with pronunciation, meanings in '
                      'English and several sentences to illustrate them.\n'
                      'Respond in the following format:\n'
                      'Word: <word> (jiǎo zi)\n'
                      'Meaning: dumplings\n'
                      '\n'
                      'Example sentences:\n'
                      '1. <sentence>\n'
                      '(<pronunciation>)\n'
                      '<translation>\n')