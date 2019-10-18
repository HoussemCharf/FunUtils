# possible replacement pyttsx3
from gtts import gTTS
import os
from utils import *
# tts audio config
PATH_TO_AUDIO_DIR = r"audio/"
DEFAULT_AUDIO_FILE = PATH_TO_AUDIO_DIR + "temporary.mp3"

#NOTE:
# install dependencies:
# pip3 install gTTS
# pip3 install playsound
class Speaker:
    def __init__(self, language="en-us"):
        self._language = language
        self._tts = gTTS(lang=self._language, text="dummy")

    # public methods
    def set_language(self, language):
        """
        Sets operating speaking _language.
        :param str language: _language code
        :rtype: None
        :return: void method
        """
        assert (isinstance(language, str))
        self._language = language
        self._tts.lang = self._language

    def get_language(self):
        """
        Returns speaking _language.
        :rtype:str
        :return: speaking _language
        """
        return self._language

    def save_speech_and_play(self, text=""):
        """
        Speak out the given text. Text must not be empty string.
        :param str text: text to be spoken
        :rtype: None
        :return: void method
        """
        assert (isinstance(text, str))
        if text != '':
            self._speak(text, str(get_current_timestamp()) + ".mp3")

    # private methods
    def _speak(self, text, file_name=DEFAULT_AUDIO_FILE):
        """
        Speak out and play audio.
        :param str text:
        :param str file_name: audio file in which speech will be saved
        :rtype: None
        :return:void method
        """
        assert (isinstance(text, str))
        if file_name != DEFAULT_AUDIO_FILE:
            file_name = PATH_TO_AUDIO_DIR + file_name
        self._tts.text = text
        self._tts.save(file_name)
        play_audio(file_name)
