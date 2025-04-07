import itertools
import json
import logging
import random
import time

from daily_dragon.handlers.constants import VOCABULARY_FILE_NAME


class Vocabulary:

    def __init__(self, user_id: id):
        self.vocabulary = dict()
        self.vocabulary_file_name = VOCABULARY_FILE_NAME.format(user_id=user_id)

    def save_word(self, word):
        # read the vocabulary file once more because it may have changed
        with open(self.vocabulary_file_name, 'r', encoding='utf-8') as file:
            self.vocabulary = json.load(file)
        logging.info(f"Loaded vocabulary from {self.vocabulary_file_name} with {len(self.vocabulary)} words.")

        if word.word in self.vocabulary.keys():
            logging.info(f"Word {word.word} already exists in vocabulary.")
            raise ValueError(f"Word {word.word} already exists in vocabulary.")
        self.vocabulary[word.word] = {
            'pronunciation': word.pronunciation,
            'translation': word.translation,
            'added_on': int(time.time())
        }

        with open(self.vocabulary_file_name, mode='w', encoding='utf-8') as file:
            json.dump(self.vocabulary, file, ensure_ascii=False, indent=4)
        logging.info(f"Word '{word}' saved to vocabulary.")

    def get_random_words(self, count: int):
        with open(self.vocabulary_file_name, 'r', encoding='utf-8') as file:
            self.vocabulary = json.load(file)

        iterator = iter(self.vocabulary)
        try:
            words = random.sample(list(itertools.islice(iterator, count * 10)), count)
        except ValueError:
            words = list(self.vocabulary.keys())

        logging.info(f"Selected random words: {words}")
        return words

    def get_all_words(self):
        with open(self.vocabulary_file_name, 'r', encoding='utf-8') as file:
            self.vocabulary = json.load(file)
        return self.vocabulary


class Word:
    def __init__(self, word, pronunciation, translation):
        self.word = word
        self.pronunciation = pronunciation
        self.translation = translation
        self.added_on = int(time.time())

    def __str__(self):
        return f"{self.word} ({self.pronunciation}) - {self.translation}"
