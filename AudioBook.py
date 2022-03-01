import pyttsx3
import PyPDF2
book = open("Business.pdf", 'rb')
pdfReader = PyPDF2.PdfFileReader(book)  #Allowing to read the book
pages = pdfReader.numPages   #To print the no of pages in book
print(pages)

speak = pyttsx3.init()
speak.say("Hello Ayush I am starting reading the book The Business of 21st Century")
for i in range(12,pages):
    page = pdfReader.getPage(11)
    text = page.extractText()
    speak.say(text)
    speak.runAndWait()