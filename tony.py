from recaudio import rec
from rectotext import rec_to_text
from search import find
rec()
question = rec_to_text()
print(find(question))

