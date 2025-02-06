import json
import logging
from json import JSONDecodeError
from typing import List

from openai import OpenAI

from openai_client import prompts
from openai_client.constants import CHAT_GPT_MODEL

logger = logging.getLogger(__name__)

LANGUAGES = {'Chinese', 'Japanese'}


class DailyDragon:
    openai_client: OpenAI
    language: str

    def __init__(self):
        self.openai_client = OpenAI()
        self.language = 'Chinese'

    def get_daily_word(self):
        prompt = prompts.get_daily_word_prompt()
        prompt = prompt.format(language=self.language)
        completion = self.openai_client.chat.completions.create(
            model=CHAT_GPT_MODEL,
            messages=[
                {"role": "system", "content": f"You are a teacher of {self.language}."},
                {"role": "user", "content": f"{prompt}"}
            ]
        )
        logger.info(completion)
        return completion.choices[0].message.content

    def get_sentences_for_practice(self, words: List[str]):
        prompt = prompts.get_sentences_for_practice_prompt()
        prompt = prompt.format(language=self.language, words=words)
        completion = self.openai_client.chat.completions.create(
            model=CHAT_GPT_MODEL,
            messages=[
                {"role": "system", "content": f"You are a teacher of {self.language}."},
                {"role": "user", "content": f"{prompt}"}
            ]
        )
        sentences = json.loads(completion.choices[0].message.content)
        logger.info(f"Generated practice sentences: {sentences}")
        return sentences

    def mark_translations(self, translations: List) -> List:
        prompt = prompts.get_mark_translations_prompt()
        prompt = prompt.format(language=self.language, translations=translations)
        logging.info("Marking translations...")
        completion = self.openai_client.chat.completions.create(
            model=CHAT_GPT_MODEL,
            messages=[
                {"role": "system", "content": f"You are a teacher of {self.language}."},
                {"role": "user", "content": f"{prompt}"}
            ]
        )
        response = completion.choices[0].message.content
        try:
            marked_translations = json.loads(response)
        except JSONDecodeError:
            logging.error(f"Failed to decode JSON: {response}")
            raise

        logging.info(f"Marked translations: {marked_translations}")
        return marked_translations

    def set_language(self, language: str):
        if language not in LANGUAGES:
            raise ValueError(f'Language {language} not supported')
        self.language = language
