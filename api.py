"""
The script for building an API to interact with `notes` module
"""
from notes import Notebook

from typing import Dict, Union
import json

from fastapi import FastAPI

from pydantic import BaseModel


nb = Notebook()
app = FastAPI()


class Input(BaseModel):
    name: str
    contents: str


@app.get('/')
def intro():
    """An introduction to usage of API"""
    msg = "This is the API of note-taking app."
    return msg

@app.get('/list')
def list_notes():
    return nb.notes()

@app.get('/find')
def search_by_term(term: str):
    return nb.find(term)

@app.get('/note/{note_name}')
def get_contents(note_name: str) -> str:
    return nb[note_name].text()

@app.post('/add/')
def add_notes(input: Input):
    nb.add(input.name, input.contents)
    return {input.name: input.contents}

