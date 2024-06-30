import pyttsx3
import time
import os
import PyPDF2
output = ""

while True:
    inputpdf = input("PDF Path: ")
    try:
        pdfFileObject = open(f'{inputpdf}', 'rb')
        pdfReader = PyPDF2.PdfReader(pdfFileObject)
        break
    except:
        print("Invalid Path")


count = len(pdfReader.pages)
for i in range(count):
    page = pdfReader.pages[i]
    output += (page.extract_text())

output = output.replace("\n", "")

#Easter Eggs :)
output = output.replace("Halo", "Halo Infinite")
output = output.replace("NO Power", "WHYYYYYYYYYYYYY, NO Power")


engine = pyttsx3.init()


rate = engine.getProperty('rate')
while True:
    rate = input("Rate [Integer]: ")
    try:
        rate = int(rate)
        break
    except:
        print("Error: Not Int")
engine.setProperty('rate', {rate})

voices = engine.getProperty('voices')
while True:
    voice = input("Voice [Integer, 0 for Man, 1 for Woman]: ")
    try:
        voice = int(voice)
        break
    except:
        print("Error: Not Int")
engine.setProperty('voice', voices[voice].id)

while True:
    path = input("Path to Save MP3: ")
    try:
        engine.save_to_file((output), (path))
        break
    except:
        print("Path Error")
engine.runAndWait()