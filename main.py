#importing python modules
#note : python modules need to be downloaded before running this program (can use pip command)
import pyttsx3
import PyPDF3
from tkinter.filedialog import *

#*using commands from the python module
#opens file explorer to select PDF
player = pyttsx3.init()
book = askopenfilename()
pdfreader = PyPDF3.PdfFileReader(book)
pages = pdfreader.numPages

#uses pyttsx3 commands to read out the text
#say(text) is used to give audio output to the user
for num in range(0, pages):
    page = pdfreader.getPage(num)
    text = page.extractText()
    player.say(text)
    player.runAndWait()