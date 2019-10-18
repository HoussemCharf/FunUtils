from stt import SpeechRecognizer

recognizer = SpeechRecognizer("en-US")
print(recognizer.recognize_from_microphone())
