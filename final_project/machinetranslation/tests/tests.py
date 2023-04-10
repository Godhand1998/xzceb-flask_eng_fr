'''Module for Unit testing E_F and F_E translations
'''
import unittest
from translator import english_to_french,french_to_english

class TestTranslatorEF(unittest.TestCase):
    '''Class for E_F unittest
    '''
    def test_english_to_french(self):
        ''' TestCases for English to French translation
        '''
        self.assertEqual(english_to_french("Hello"),"Bonjour")
        self.assertEqual(english_to_french("I am smart boy"),"Je suis un garçon intelligent")
        self.assertEqual(english_to_french(" ")," ")
        self.assertNotEqual(english_to_french("Hello"),"Hello")

class TestTranslatorFE(unittest.TestCase):
    '''Class for F_E unittest
    '''
    def test_french_to_english(self):
        '''TestCases for French to English translation
        '''
        self.assertEqual(french_to_english("Bonjour"),"Hello")
        self.assertEqual(french_to_english("Je suis un garçon intelligent"),"I am an intelligent boy")
        self.assertEqual(french_to_english(" ")," ")
        self.assertNotEqual(french_to_english("Bonjour"),"Bonjour")

unittest.main()

