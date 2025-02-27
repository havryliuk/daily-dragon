from openai_client.prompts import get_daily_word_prompt, get_sentences_for_practice_prompt, get_mark_translations_prompt


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


def test_get_sentences_for_practice_prompt():
    prompt = get_sentences_for_practice_prompt()
    assert prompt == """Give me sentences to practice translation from English to {language}.
Here are the words to use in the sentences: {words}.
Generate one sentence for each word. Don't use the same word in multiple sentences.
Enclose the translated English words in angle brackets.
The example sentences must be in English!

Example:
{{"sentences": [{{"word": "运动", "sentence": "I like to <exercise> every day."}}, {{"word": "学习", "sentence": "I <study> Chinese at school."}}]}}
"""


def test_get_mark_translations_prompt():
    prompt = get_mark_translations_prompt()
    assert prompt == """Provided these sentences and their translations to {language} for a word:
{translations}
mark the translations from 0 to 10. the main criteria is whether the correct word was used for the underlined word. add comment if necessary
add two more fields to each object: "mark": 10 having the mark and "comment": "comment"
example (return only json as text without json formatting tag)!:
[{{ "sentence": "The hotel is in the city center.", "translation": "酒店在市中心", "word": "市中心", "mark": "mark", "comment": "comment" }}]"""
