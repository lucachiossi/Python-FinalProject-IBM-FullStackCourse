"""
test_translator.py
"""

import unittest
from src.translator import english_to_french, english_to_german

class TestTranslator(unittest.TestCase):
    """
    class testing module translator
    """
    def test_english_to_french_null_input(self):
        """
        test function english_to_french behavior with null input
        """
        self.assertIsNone(english_to_french(None))

    def test_english_to_french_hello_word(self):
        """
        test function english_to_french behavior with the word 'Hello'
        """
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

    def test_english_to_french_1(self):
        """
        test function english_to_french
        """
        self.assertEqual(english_to_french('It is time to code'), 'Il est temps de coder')

    def test_english_to_german_null_input(self):
        """
        test function english_to_german behavior with null input
        """
        self.assertIsNone(english_to_german(None))

    def test_english_to_german_hello_word(self):
        """
        test function english_to_german behavior with the word 'Hello'
        """
        self.assertEqual(english_to_german('Hello'), 'Hallo')

    def test_english_to_german_1(self):
        """
        test function english_to_german
        """
        self.assertEqual(english_to_german('It is time to code'), 'Es ist Zeit zum Code')
