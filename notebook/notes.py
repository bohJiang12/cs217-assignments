"""
The module implements a note-taking app, and it supports following functions:
    * Add a note into existing notebook
    * List all existing notes
    * Find a note by searching user-provided term(s)
    * Display contents of a note from user-entered note's name

In general, this note-taking app (or say notebook) has the following scheme:
---
Notebook
    |___ Note
        |--- name
        |--- contents
---
"""

"""
TODO:

- [x] Create a new note
- [x] Show only names of all existing notes
- [x] Show only names of notes (&their comments) containing given term
- [x] Given a note's name, return its contents and related comments
- [x] Delete a note with its comments
- [x] Add a comment to a note
"""


from typing import List, Set
from datetime import datetime
from sqlalchemy.exc import IntegrityError
from notebook.model import Note, Comment
from notebook import db, app


class Notebook:
    """Notebook kernel interacting between Flask web server and backend database"""

    @staticmethod
    def show_all_note_names() -> List[Note]:
        """Display names of existing notes in database"""
        return db.session.query(Note.name).all()

    @staticmethod
    def add_note(name: str, text: str):
        """Add a new note with new titie and contents"""
        try:
            note = Note(name=name, text=text)
            db.session.add(note)
            db.session.commit()
            return True
        except IntegrityError as e:
            db.session.rollback()
            return e

    @staticmethod
    def add_comment(text: str, note_id: int) -> Comment | None:
        """Add a comment to a note by providing its id"""
        
        # Sanity check even though assuming its tailored note exists
        note = db.session.execute(
            db.select(Note).filter_by(id=note_id)
        ).first()

        if not note:
            print(f'Queried note (id={note_id}) does not exist')
            return None

        utn = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_comment = Comment(text=text, date=utn, note_id=note_id)
        db.session.add(new_comment)
        db.session.commit()
        return new_comment

    @staticmethod
    def find(term: str) -> Set[Note]:
        """Find a note (and its comments) that contains provided term"""
        match_pattern = f"\\b{term}\\b"
        notes_found = Note.query.filter(Note.text.op('REGEXP')(match_pattern)).all()
        comments_found = db.session.query(Note).join(Comment).filter(
            Comment.text.op('REGEXP')(match_pattern)
        ).all()

        return set(notes_found + comments_found)

    @staticmethod
    def fetch_note(name: str) -> Note | None:
        """Fetch a note by the provided name"""
        note = Note.query.filter_by(name=name).first()

        if not note:
            return None
        else:
            return note

    @staticmethod
    def clear():
        db.session.query(Note).delete()
        db.session.query(Comment).delete()
        db.session.commit()

    @staticmethod
    def delete_note(note_id: int):
        """Delete a note and its comment given its id"""
        note = db.session.query(Note).filter_by(id=note_id).first()
        assert note is not None

        try:
            db.session.delete(note)
            db.session.commit()
        except IntegrityError as e:
            return e
