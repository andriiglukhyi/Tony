from recaudio import rec
from rectotext import rec_to_text
from search import find
from gtts import gTTS
import os
import pygame
import time

rec('record.wav')
question = rec_to_text()
answer = find(question)
tts = gTTS(text=answer, lang='en')
tts.save("good.mp3")
pygame.init()
pygame.mixer.music.load("good.mp3")
pygame.mixer.music.play()
time.sleep(5)

