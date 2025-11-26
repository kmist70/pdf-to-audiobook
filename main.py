import pyttsx3
from PyPDF2 import PdfReader

pdf = open("sample.pdf", 'rb')     # first parameter is the name of the PDF file
pdf_reader = PdfReader(pdf) 

print("Welcome to Text-To-Speech!")
text_to_speech = pyttsx3.init()
rate = 200  # 200 WPM is the default rate of speech

read_more_pages = True
while read_more_pages:
    print("Ex: To read a specific page, enter the current page number (in the PDF reader, not the actual PDF).\n")
    while True:
        try:
            page_num = int(input("Enter page number: "))
            page_num -= 1
            if 0 <= page_num < len(pdf_reader.pages):
                break
            else:
                print("Please enter a valid integer!\n")
        except ValueError:
            print("Invalid input! Please enter a valid integer!\n")

    page_to_read = pdf_reader.pages[page_num]

    change_rate = input(f"The current speech rate is {rate} WPM.\nWould you like to change the speech rate? Enter 'YES' to change it: ")
    if change_rate.lower() in ["yes", "y"]:
        rate = int(input("Enter new speech rate (the default is 200 WPM): "))
        while True:
            try:
                text_to_speech.setProperty('rate', rate)
                break
            except ValueError:
                print("Invalid input! Please enter a valid integer!\n")

    text = page_to_read.extract_text()
    text_to_speech.say(text)
    print("\nYou can stop the speech process at anytime by pressing Ctrl + C\n")
    try:
        text_to_speech.runAndWait()
    except KeyboardInterrupt:
        text_to_speech.stop()
        print("Speech has been terminated.\n")
    
    answer = input("Would you like to read more pages? Enter 'YES' to continue: ")
    if answer.lower() not in ["yes", "y"]:
        read_more_pages = False
    print("\n")

print("Thank you for using Text-To-Speech!\n")
pdf.close()    # closes the PdfReader object