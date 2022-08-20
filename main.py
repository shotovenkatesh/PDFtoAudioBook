from gtts import gTTS
from playsound import playsound
from PyPDF2 import PdfReader

reader = PdfReader("test.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()

#
language = 'en'

obj = gTTS(text=text, lang=language, slow=False)
obj.save("test_audio.mp3")
playsound("test_audio.mp3")