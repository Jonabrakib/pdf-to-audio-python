import pyttsx3
import PyPDF2
book = open('read.pdf','rb')

pdfReader=PyPDF2.PdfFileReader(book)
page=pdfReader.getPage(2)
text=page.extractText()

initialize = pyttsx3.init()
initialize.say(text)
initialize.runAndWait()