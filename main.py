from PyPDF2 import PdfFileReader, PdfFileWriter

actions = ["Split every page", "Split PDF in certain page",
           "Merge PDFs", "Encrypt PDF"]


# helping functions
def show_menu():
    i = 1
    print("\n")
    for action in actions:
        print(
            str(i) + ". " + action
        )
        i += 1


def split_every_page():
    pdf_input = input("\nEnter the name of the PDF file you want to split: (example: myPDF) ")
    pdf_input = pdf_input+".pdf"
    pdf_output = input("\nEnter the name you want for the split file: (example: mySplitPDF) ")
    pdf_reader = PdfFileReader(pdf_input)

    for page in range(pdf_reader.getNumPages()):
        pdf_writer = PdfFileWriter()
        curr_page = pdf_reader.getPage(page)
        pdf_writer.addPage(curr_page)
        new_pdf = open(pdf_output + str(page+1) + ".pdf", "wb")
        pdf_writer.write(new_pdf)
        new_pdf.close()

    return 0


def split_pdf_in_certain_page():
    pdf_input = input("\nEnter the name of the PDF file you want to split: (example: myPDF) ")
    pdf_input = pdf_input + ".pdf"
    split_number = int(input("\nOn which page would you like to split the file? \n"
                             "(for example: for the number 3 -> first PDF contains pages 1,2,3 and second PDF contains the rest"))
    pdf_output = input("\nEnter the name you want for the split file: (example: mySplitPDF) ")
    pdf_reader = PdfFileReader(pdf_input)
    pdf_writer = PdfFileWriter()
    for page in range(split_number):
        curr_page = pdf_reader.getPage(page)
        pdf_writer.addPage(curr_page)
    new_pdf = open(pdf_output + "1.pdf", "wb")
    pdf_writer.write(new_pdf)

    pdf_writer = PdfFileWriter()
    for page in range(split_number, pdf_reader.getNumPages()):
        curr_page = pdf_reader.getPage(page)
        pdf_writer.addPage(curr_page)
    new_pdf = open(pdf_output + "2.pdf", "wb")
    pdf_writer.write(new_pdf)
    new_pdf.close()
    return 0


def merge_pdf():        # pdf1.pdf pdf2.pdf
    pdf_input = input("\nEnter the names of the PDF files you want to merge: (example: myPDF1 myPDF2 myPDF3) ")
    pdf_output = input("\nEnter the name you want for the merged file: (example: myMergedPDF) ")
    pdf_list = pdf_input.split(" ")
    pdf_writer = PdfFileWriter()
    for file in pdf_list:
        file = file+".pdf"
        pdf_reader = PdfFileReader(file)
        for page in range(pdf_reader.getNumPages()):
            curr_page = pdf_reader.getPage(page)
            pdf_writer.addPage(curr_page)
    merged = open(pdf_output+".pdf", "wb")
    pdf_writer.write(merged)
    merged.close()
    return 0


def encrypt_pdf():
    pdf_input = input("\nEnter the name of the PDF file you want to encrypt: (example: myPDF) ")
    pdf_input = pdf_input + ".pdf"
    pdf_password = input("\nEnter a password that will be used to encrypt the file: ")
    pdf_output = input("\nEnter the name you want for the encrypted file: (example: myEncryptedPDF) ")
    pdf_reader = PdfFileReader(pdf_input)
    pdf_writer = PdfFileWriter()
    for page in range(pdf_reader.getNumPages()):
        curr_page = pdf_reader.getPage(page)
        pdf_writer.addPage(curr_page)

    pdf_writer.encrypt(user_pwd=pdf_password, use_128bit=True)

    new_pdf = open(pdf_output+".pdf", "wb")
    pdf_writer.write(new_pdf)
    new_pdf.close()
    return 0


# main function
def handle_pdf():

    show_menu()
    while True:
        action = int(input("\nWhat do you want to do? (click 0 if you want to quit) "))
        if action == 0:
            return 0
        if action == 1:
            split_every_page()
            return 0
        if action == 2:
            split_pdf_in_certain_page()
            return 0
        if action == 3:
            merge_pdf()
            return 0
        if action == 4:
            encrypt_pdf()
            return 0
        else:
            print("invalid choice")


if __name__ == "__main__":
    handle_pdf()






