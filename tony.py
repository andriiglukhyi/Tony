from recaudio import rec
from rectotext import rec_to_text
from search import find
from gtts import gTTS
import os



rec()
question = rec_to_text()
answer = find(question)
tts = gTTS(text=answer, lang='en')
tts.save("good.mp3")
os.system("mpg321 good.mp3")