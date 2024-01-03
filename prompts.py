def get_daily_word_prompt():
    with (open('prompts/daily_word', 'r', encoding='utf-8')) as file:
        return file.read()
