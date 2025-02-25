"""
The script for building an API to interact with `notes` module
"""
from notes import Notebook

from typing import Dict, Union

from fastapi import FastAPI

from pydantic import BaseModel


nb = Notebook()
app = FastAPI()


class Input(BaseModel):
    name: str
    contents: str


@app.get('/')
def intro():
    """
    An introduction to usage of API

    Usage:
        http://127.0.0.1:8000
    """
    msg = "This is the API of note-taking app."
    return msg

@app.get('/list')
def list_notes():
    """Page of listing existing notes

    Returns:
        None

    Usage:
        http://127.0.0.1:8000/list
    """
    return nb.notes()

@app.get('/find')
def search_by_term(term: str):
    """Page of listing existing notes that contain the provided term

    Args:
        term: a string to search for

    Returns:
        a list of notes' names

    Usage:
        http://127.0.0.1:8000/find?term=<term>
    """
    return nb.find(term)

@app.get('/note/{note_name}')
def get_contents(note_name: str) -> str:
    """Page of displaying note contents by providing its note's name

    Args:
        note_name: a string of note's name

    Returns:
        note's contents

    Usage:
        http://127.0.0.1:8000/note/<note_name>
    """
    return nb[note_name].text()

@app.post('/add')
def add_notes(input: Input):
    """POST method for adding a new note

    Args:
        input: a new note as an `Input` object

    Returns:
        None

    Usage:
        curl -X 'POST' \
            'http://127.0.0.1:8000/add' \
            -H 'accept: application/json' \
            -H 'Content-Type: application/json' \
            -d '{
            "name": "Remember my cheese",
            "contents": "I want both Gouda and Cheddar"
            }'
    """
    nb.add(input.name, input.contents)
    return {input.name: input.contents}

