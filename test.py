import unittest
from notebook import notes, app, db
from notebook.model import Comment, Note
from notebook.notes import Notebook

class TestNotebook(unittest.TestCase):
    """Unit test for `Notebook` class"""

    @classmethod
    def setUpClass(cls):
        app.config["SQLALCHEMY_DATABASE_URI"]= "sqlite:///:memory"
        app.config["TESTING"] = True

        with app.app_context():
            db.init_app(app)
            db.create_all()

    @classmethod
    def tearDownClass(cls):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def setUp(self):
        with app.app_context():
            db.session.query(Comment).delete()
            db.session.query(Note).delete()
            db.session.commit()

    def test_add_note(self):
        with app.app_context():
            Notebook.add_note("note_1", "Mon")
            added_note = db.session.query(Note).first()

            self.assertIsNotNone(added_note)
            self.assertEqual(added_note.name, 'note_1')
            self.assertEqual(added_note.text, 'Mon')
            self.assertEqual(db.session.query(Note).count(), 1)

    def test_add_comment(self):
        with app.app_context():
            Notebook.add_note('test', 'a note for test')
            added_note = db.session.query(Note).first()

            Notebook.add_comment(text='testing', note_id=added_note.id)
            added_comment = db.session.query(Comment).first()

            self.assertIsNotNone(added_comment)
            self.assertEqual(added_comment.text, 'testing')
            self.assertEqual(added_comment.note_id, added_note.id)

    def test_find_note(self):
        with app.app_context():
            Notebook.add_note('note_1', 'it is rainy today.')
            Notebook.add_note('note_2', 'it is sunny today.')
            Notebook.add_note('note_3', 'it is cloudy today.')

            note_1 = db.session.execute(
                db.select(Note).filter_by(name='note_1')
            ).scalar_one()
            note_2 = db.session.execute(
                db.select(Note).filter_by(name='note_2')
            ).scalar_one()
            note_3 = db.session.execute(
                db.select(Note).filter_by(name='note_3')
            ).scalar_one()

            Notebook.add_comment('comment 1', note_1.id)
            Notebook.add_comment('comment 2', note_2.id)
            Notebook.add_comment('comment 3', note_3.id)

            self.assertEqual({note_1}, Notebook.find('rainy'))
            self.assertEqual({note_2}, Notebook.find('sunny'))
            self.assertEqual({note_3}, Notebook.find('cloudy'))
            self.assertEqual({note_1, note_2, note_3}, Notebook.find('today'))
            self.assertEqual({note_1, note_2, note_3}, Notebook.find('comment'))

    def test_fetch_note(self):
        with app.app_context():
            Notebook.add_note('note_1', 'it is rainy today.')
            note_1 = db.session.execute(
                db.select(Note).filter_by(name='note_1')
            ).scalar_one()
            Notebook.add_comment('comment 1', note_1.id)

            self.assertEqual(note_1, Notebook.fetch_note('note_1'))
            self.assertEqual(None, Notebook.fetch_note('note_2'))

    def test_delete_note(self):
        with app.app_context():
            Notebook.add_note('note_1', 'it is rainy today.')
            Notebook.add_note('note_2', 'it is sunny today.')
            Notebook.add_note('note_3', 'it is cloudy today.')

            Notebook.delete_note(note_id=1)
            self.assertEqual(db.session.query(Note).count(), 2)

            Notebook.delete_note(note_id=2)
            self.assertEqual(db.session.query(Note).count(), 1)

            Notebook.delete_note(note_id=3)
            self.assertEqual(db.session.query(Note).count(), 0)

    def test_clear(self):
        with app.app_context():
            Notebook.add_note('note_1', 'it is rainy today.')
            Notebook.add_note('note_2', 'it is sunny today.')
            Notebook.add_note('note_3', 'it is cloudy today.')

            Notebook.clear()
            self.assertEqual(db.session.query(Note).count(), 0)


if __name__ == '__main__':
    unittest.main()
