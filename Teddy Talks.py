from gtts import gTTS
tts = gTTS('hi', lang='en')
tts.save('hello.mp3')