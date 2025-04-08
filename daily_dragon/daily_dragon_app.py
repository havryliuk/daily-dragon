import logging

from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel

from daily_dragon.exceptions import WordAlreadyExistsError
from daily_dragon.service.vocabulary_service import VocabularyService

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

app = FastAPI()


class WordEntry(BaseModel):
    word: str


@app.post("/vocabulary", status_code=201)
def add_word(word_entry: WordEntry, vocabulary_service: VocabularyService = Depends()):
    word = word_entry.word
    try:
        vocabulary_service.add_word(word_entry.word)
        return {"message": f"Word {word} added to vocabulary"}
    except WordAlreadyExistsError:
        raise HTTPException(status_code=409, detail=f"Word {word} already exists")


@app.get("/vocabulary")
def get_vocabulary(vocabulary_service: VocabularyService = Depends()):
    vocabulary = vocabulary_service.get_vocabulary()
    return vocabulary


@app.delete("/vocabulary/{word}")
def delete_word(word: str, vocabulary_service: VocabularyService = Depends()):
    vocabulary_service.delete_word(word)
