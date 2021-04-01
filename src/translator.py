"""
translator.py
"""

import os
# import json

from dotenv import load_dotenv, find_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

def english_to_french(english_text):
    """
    this function translates english text to
    french text using IBM WLT service
    """
    # get service authentication credentials
    load_dotenv(find_dotenv())
    api_key = os.getenv('API_KEY')
    api_url = os.getenv('API_URL')

    # authenticate with cloud service
    authenticator = IAMAuthenticator(api_key)
    language_translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=authenticator
        )
    language_translator.set_service_url(api_url)

    # return text translation
    translation = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
    french_text = translation['translations'][0]['translation']
    return french_text
