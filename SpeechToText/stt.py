import speech_recognition as sr
from config.config import *
from services.common.action_result import ActionResult

#dependency - SpeechRecognition lib https://github.com/Uberi/speech_recognition - pip3 install SpeechRecognition
#convert speech to text from microphone audio
class SpeechRecognizer:

    def __init__(self, recognition_api="google", language="en-us"):
        self._recognizer = sr.Recognizer()
        # below energy_threshold is considered silence, above speech
        self._recognizer.energy_threshold = 500
        self._recognition_api = recognition_api
        self._recognition_method = None
        self._determine_recognition_method()
        self._microphone = sr.Microphone()
        self._language = language

    # public methods
    def set_language(self, language):
        """
        Sets recognition _language.
        :param str language: _language code
        :rtype: None
        :return: void method
        """
        assert (isinstance(language, str))
        self._language = language

    def get_language(self):
        """
        Returns recognition _language.
        :rtype:str
        :return: recognition _language
        """
        return self._language

    def recognize_from_microphone(self):
        """
        Returns action result with recognized text from the speech. Input speech is read from microphone. Raises RequestError or
        UnknownValueError.
        :rtype: ActionResult
        :return: ActionResult with recognized text from the speech
        """
        audio = self._get_audio_from_microphone()
        speech = self._recognition_method(audio, language=self._language)
        result = ActionResult(speech, SUCCESS)
        return result

    # private methods
    def _determine_recognition_method(self):
        """
        Determines and sets recognition method - based on the API name.
        :rtype: None
        :return: void method
        """
        api_method = RECOGNITION_METHODS.get(self._recognition_api, "recognize_google")
        if self._recognizer is not None and hasattr(self._recognizer, api_method):
            self._recognition_method = getattr(self._recognizer, api_method)

    # NOTE: not implemented
    def _recognize_from_file(self, audio_file):
        pass

    def _get_audio_from_microphone(self):
        """
        Returns audio data from the microphone
        :rtype: AudioData
        :return:
        """
        audio = None
        if self._microphone is not None:
            with self._microphone as source:
                print('Ready for command...')
                logger.info("Ready for command...")
                self._recognizer.adjust_for_ambient_noise(source)
                audio = self._recognizer.listen(source)
                logger.debug("Audio data = {}".format(audio))
        return audio
