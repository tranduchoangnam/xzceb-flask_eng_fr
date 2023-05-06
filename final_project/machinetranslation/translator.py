import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

url = os.environ['url']
apikey = os.environ['apikey']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    """
    Translates English text to French.

    Args:
        englishText (str): The text to translate.

    Returns:
        str: The translated text in French.
    """
    #write the code here
    try:
        translation = language_translator.translate(
            text=english_text, source='en', target='fr').get_result()
    except:
        return None
    french_text = translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    """
    Translates French text to English.

    Args:
        frenchText (str): The text to translate.

    Returns:
        str: The translated text in English.
    """
    #write the code here
    try:
        translation = language_translator.translate(
            text=french_text, source='fr', target='en').get_result()
    except:
        return None
    english_text = translation['translations'][0]['translation']
    return english_text
