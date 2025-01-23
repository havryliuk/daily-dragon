import json
import logging


class Vocabulary:

    def __init__(self, file_name: str):
        self.vocabulary = dict()
        self.vocabulary_file_name = file_name

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
            'translation': word.translation
        }

        with open(self.vocabulary_file_name, mode='w', encoding='utf-8') as file:
            json.dump(self.vocabulary, file, ensure_ascii=False, indent=4)
        logging.info(f"Word '{word}' saved to vocabulary.")


class Word:
    def __init__(self, word, pronunciation, translation):
        self.word = word
        self.pronunciation = pronunciation
        self.translation = translation

    def __str__(self):
        return f"{self.word} ({self.pronunciation}) - {self.translation}"
