import logging

from dotenv import load_dotenv
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel

from daily_dragon.auth.authenticate import authenticate
from daily_dragon.exceptions import WordAlreadyExistsError
from daily_dragon.service.vocabulary_service import VocabularyService

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

load_dotenv()

app = FastAPI()


class WordEntry(BaseModel):
    word: str


@app.post("/daily-dragon/vocabulary", status_code=201)
def add_word(word_entry: WordEntry, vocabulary_service: VocabularyService = Depends(),
             username: str = Depends(authenticate)):
    word = word_entry.word
    try:
        vocabulary_service.add_word(word_entry.word)
        return {"message": f"Word {word} added to vocabulary"}
    except WordAlreadyExistsError:
        raise HTTPException(status_code=409, detail=f"Word {word} already exists")


@app.get("/daily-dragon/vocabulary")
def get_vocabulary(vocabulary_service: VocabularyService = Depends(), username: str = Depends(authenticate)):
    vocabulary = vocabulary_service.get_vocabulary()
    return vocabulary


@app.delete("/daily-dragon/vocabulary/{word}")
def delete_word(word: str, vocabulary_service: VocabularyService = Depends(), username: str = Depends(authenticate)):
    vocabulary_service.delete_word(word)
    return {"message": f"Word {word} deleted"}
