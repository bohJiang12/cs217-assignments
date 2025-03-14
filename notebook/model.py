"""
The module implements for the database model of note-taking app

This module contains two classes:
- `Note` class is a DB storing notes within a notebook
- `Comment` class is a DB storing comments for a note
"""

from notebook import db
from datetime import datetime


class Note(db.Model):
    """
    Database of notes taken in the app

    Scheme:
    id      name    text
    ---------------------
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    text = db.Column(db.String(120), nullable=False)
    comments = db.relationship('Comment', backref='note', cascade='all, delete')

    def __repr__(self) -> str:
        return f"Note(id={self.id} name={self.name} comments={self.comments})"


class Comment(db.Model):
    """
    Database of comments added to a note

    Scheme:
    id      text    date    note_id
    ---------------------------------
    """

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(20), nullable=False)
    note_id = db.Column(db.Integer, db.ForeignKey('note.id', ondelete="CASCADE"), nullable=False)

    def __repr__(self) -> str:
        return f"Comment(id={self.id}, text={self.text}, date={self.date}, note_id={self.note_id})"








