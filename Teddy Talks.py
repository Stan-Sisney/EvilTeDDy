from gtts import gTTS
tts = gTTS('hello this is STARK and i am a sexy bitch!', lang='en')
tts.save('hello.mp3')