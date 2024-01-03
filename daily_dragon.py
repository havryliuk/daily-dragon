from openai import OpenAI

import prompts

LANGUAGES = {'Chinese', 'Japanese'}


class DailyDragon:
    openai_client: OpenAI
    language: str

    def __init__(self):
        self.openai_client = OpenAI()
        self.language = 'Chinese'

    def get_daily_word(self):
        prompt = prompts.get_daily_word_prompt()
        prompt = prompt.replace('${language}', self.language)
        print(prompt)
        completion = self.openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"You are a teacher of ${self.language}."},
                {"role": "user", "content": f"${prompt}"}
            ]
        )
        return completion.choices[0].message.content

    def set_language(self, language: str):
        if language not in LANGUAGES:
            raise ValueError(f'Language {language} not supported')
        self.language = language
