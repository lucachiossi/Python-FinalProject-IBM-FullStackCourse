"""
test_translator.py
"""

import unittest
from src.translator import english_to_french, english_to_german

class TestTranslator(unittest.TestCase):
    """
    class testing module translator
    """
    def test_english_to_french(self):
        """
        test function english_to_french
        """
        self.assertEqual(english_to_french('Hello my friend'), 'Bonjour mon ami')
        self.assertEqual(english_to_french('Help, please'), "Aide, s'il vous plaît")
        self.assertEqual(english_to_french('It is time to code'), 'Il est temps de coder')

    def test_english_to_german(self):
        """
        test function english_to_german
        """
        self.assertEqual(english_to_german('Hello my friend'), 'Hallo mein Freund')
        self.assertEqual(english_to_german('Help, please'), 'Hilfe, bitte.')
        self.assertEqual(english_to_german('It is time to code'), 'Es ist Zeit zum Code')
