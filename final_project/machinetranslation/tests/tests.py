import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from translator import english_to_french, french_to_english
import unittest

class TestTranslator(unittest.TestCase):
    def test_english_to_french_hello(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
    def test_english_to_french_goodbye(self):
        self.assertEqual(english_to_french('Goodbye'), 'Au revoir')

    def test_french_to_english_bonjour(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
    def test_french_to_english_aurevoir(self):
        self.assertEqual(french_to_english('Au revoir'), 'Goodbye')

    def test_english_to_french_null_input(self):
        self.assertEqual(english_to_french(None), None)

    def test_french_to_english_null_input(self):
        self.assertEqual(french_to_english(None), None)
        
    
        
if __name__ == '__main__':
    unittest.main()
