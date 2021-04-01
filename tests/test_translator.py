"""
test_translator.py
"""

import unittest
from src.translator import english_to_french

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
