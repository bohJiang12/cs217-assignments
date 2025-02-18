import unittest

from notes import (
    Note,
    Notebook,
    DEFAULT_FILE,
    CACHE_DIR
)

class TestNote(unittest.TestCase):
    """Test `Note` class"""

    def setUp(self):
        self.true_name, self.true_text = 'nlp', 'system'
        self.note = Note(self.true_name, self.true_text)

    def test_init_note(self):
        self.assertEqual(self.true_name, self.note.name())
        self.assertEqual(self.true_text, self.note.text())

    def test_update(self):
        new_note = 'statistics'
        self.note.update(new_note)
        self.assertEqual(self.true_name, self.note.name())
        self.assertEqual(new_note, self.note.text())


class TestNotebook(unittest.TestCase):
    """Test `Notebook` class"""

    def setUp(self):
        if CACHE_DIR.exists() and any(CACHE_DIR.iterdir()):
            for file in CACHE_DIR.glob('*'):
                if file.is_file():
                    file.unlink()

        self.nb = Notebook()

    def test_init_nb(self):
        """
        To test:
            * if `.cache` directory is created
            * if there's no note added
        """
        self.assertTrue(CACHE_DIR.exists())
        self.assertEqual(0, len(self.nb.notes()))

    def test_add_note(self):
        """
        To test the function of adding notes:
            * `.cache` directory has modified `.pkl` file
            * length of notebook is enlarged
        """
        new_name, new_text = 'Wed', 'No class today.'

        # Test the very first add
        self.nb.add(new_name, new_text)
        self.assertEqual(1, len(self.nb.notes()))

        # Test the second add
        second_name, second_text = 'Fri', 'Tomorrow is weekend.'
        self.nb.add(second_name, second_text)

        self.assertEqual(2, len(self.nb.notes()))

    def test_search_notes(self):
        """
        Test the function for search notes given a term that might be in the note
        """
        self.nb.add('1', 'Today is Friday.')
        self.nb.add('2', 'I passed my exam!')
        self.nb.add('3', "It's Friday, but I have work to do.")

        self.assertEqual(['1', '3'], self.nb.find('friday'))
        self.assertEqual(['2'], self.nb.find('exam'))
        self.assertEqual([], self.nb.find('Monday'))

    def test_search_by_term(self):
        """
        Test the behavior of searching matched notes given a term
        """
        self.nb.add(name='Wed', text="It's a rainy day.")
        self.assertEqual(['Wed'], self.nb.find('rainy'))
        self.assertEqual([], self.nb.find('sunny'))

    def test_list_notes(self):
        """
        Test the functionality of listing current notes in notebook
        """
        # when it's empty
        self.assertEqual(0, len(self.nb.notes()))
        self.assertEqual([], self.nb.notes())

        # when non-empty
        self.nb.add('1', 'first')
        self.nb.add('2', 'second')
        self.assertEqual(['1', '2'], self.nb.notes())







if __name__ == '__main__':
    unittest.main()
