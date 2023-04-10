#import json
'''Module for E_F and F_E translation
'''
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv


load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('ziSRV0B9XqUAMfdYjFSUkLdIfChnmPQl1fJ-mzvIDNus')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url\
('https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/fb04533e-75e9-4a75-b689-3420ab9cd7a1')

def english_to_french(english_text):
    #write the code here
    '''English to French translation
    '''
    translation_french = language_translator.translate\
    (text=english_text,model_id='en-fr').get_result()
    return translation_french['translations'][0]['translation']

def french_to_english(french_text):
    #write the code here
    '''French to English translation
    '''
    translation_english = language_translator.translate\
    (text=french_text,model_id='fr-en').get_result()
    return translation_english['translations'][0]['translation']
print(english_to_french("i am smart boy"))
