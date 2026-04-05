from gtts import gTTS

text = "Hello World"
tts = gTTS(text, lang='en')
tts.save("hello.mp3")