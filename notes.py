"""
The module implements a note-taking app, and it supports following functions:
    * Add a note into existing notebook
    * List all existing notes
    * Find a note by searching user-provided term(s)
    * Display contents of a note from user-entered note's name

TODO:
    - [ ] decision for loading last session or new session

In general, this note-taking app (or say notebook) has the following scheme:
---
Notebook
    |___ Note
        |--- name
        |--- contents
---
"""

from typing import Dict, List

import pickle as pkl
from pathlib import Path

from nltk.tokenize import RegexpTokenizer


CACHE_DIR = Path.cwd() / '.cache'
DEFAULT_FILE = Path('recent_notes.pkl')


class Note:
    """Note class consisting of `name` and `contents` attributes"""

    def __init__(self, name: str, contents: str):
        self._name = name
        self._text = contents

    def text(self) -> str:
        """Return the contents of the note"""
        return self._text

    def name(self):
        """Return the name of the note"""
        return self._name

    def update(self, new_text: str):
        """Update note's contents"""
        self._text = new_text


class Notebook:
    """Notebook class containing `Note` objects"""
    def __init__(self):
        self._notes: Dict[str, Note] = self._load_cache_notes()
        self._inv_notes: Dict[str, str] = {note.text(): name for name, note in self._notes.items()}

    def __setitem__(self, note_name, new_contents):
        self._notes[note_name].update(new_contents)
        self._auto_save()

    def __getitem__(self, note_name: str) -> Note:
        """Retrieve `Note` object by its name as string"""
        return self._notes.get(note_name, Note('', ''))

    def _load_cache_notes(self):
        """
        Check and load notes from last session
        """
        # Check if the cache directory exists first,
        # then check if there's any cached notes from last session
        if CACHE_DIR.exists():
            cached_notes = CACHE_DIR / DEFAULT_FILE
            try:
                with open(cached_notes, 'rb') as f:
                    return pkl.load(f)
            except FileNotFoundError:
                return {}

        # Otherwise, create a cache directory
        CACHE_DIR.mkdir()

        return {}

    def _auto_save(self):
        """
        Auto-save the notebook into cached file at real time
        ---
        The function will only be called when
            * new note is added
            * existing note is updated
        """
        assert self._notes is not None

        with open(CACHE_DIR / DEFAULT_FILE, 'wb') as f:
            # noinspection PyTypeChecker
            pkl.dump(self._notes, f)

    def notes(self):
        """
        Return names of existing notes

        >>> nb = Notebook()
        >>> nb.add('1', 'first')
        True
        >>> nb.add('2', 'second')
        True
        >>> nb.notes()
        {'1', '2'}
        """
        return [note for note in self._notes]

    def add(self, name: str, text: str) -> bool:
        """
        Add new notes with given name and text

        >>> nb = Notebook()
        >>> nb.add('nlp', 'system')
        True
        """
        self._notes.update({name: Note(name, text)})
        self._inv_notes.update({text: name})
        self._auto_save()

        return True

    def find(self, term: str) -> List[str]:
        """
        Find a `Note` object from the provided term

        Usage:
        ---
        Given the notebook has only one note, which is {name: Wed, text: It's a rainy day.}

        >>> nb = Notebook()
        >>> nb.add(name='Wed', text="It's a rainy day.")
        True
        >>> nb.find('rainy')
        ['Wed']
        >>> nb.find('sunny')
        []

        :param term: user-provided term that might be in a note
        :return: a list of `Note` objects that contains provided term
        """

        results = []
        tokenizer = RegexpTokenizer(r'\w+')

        for text, name in self._inv_notes.items():
            bow = set(tokenizer.tokenize(text.lower()))
            if term in bow:
                results.append(name)

        return results
