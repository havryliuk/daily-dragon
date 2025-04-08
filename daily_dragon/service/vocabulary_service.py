import logging

from fastapi import Depends

from daily_dragon.repository.vocabulary_repository import VocabularyRepository


class VocabularyService:

    def __init__(self, vocabulary_repository: VocabularyRepository = Depends()):
        self.vocabulary_repository = vocabulary_repository

    def add_word(self, word):
        return self.vocabulary_repository.add_word(word)

    def get_vocabulary(self):
        return self.vocabulary_repository.get_vocabulary()

    def delete_word(self, word):
        vocabulary = self.vocabulary_repository.get_vocabulary()
        if word in vocabulary:
            del vocabulary[word]
            self.vocabulary_repository.save_vocabulary(vocabulary)
        logging.info(f"Deleted word {word}")
