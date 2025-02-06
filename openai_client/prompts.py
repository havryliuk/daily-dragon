def get_daily_word_prompt():
    with (open('prompts/daily_word', 'r', encoding='utf-8')) as file:
        return file.read()


def get_sentences_for_practice_prompt():
    with (open('prompts/sentences_for_practice', 'r', encoding='utf-8')) as file:
        return file.read()


def get_mark_translations_prompt():
    with (open('prompts/mark_translations', 'r', encoding='utf-8')) as file:
        return file.read()