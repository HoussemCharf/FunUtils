from tts import Speaker

speaker = Speaker("en-us")
print(speaker._speak("Marry had a little lamb!"))
print(speaker.save_speech_and_play(text="Hello, world!"))
