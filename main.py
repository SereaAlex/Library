#This will be a dynamic library for choosing , select and add pdfs as books

import os
from PyPDF2 import PdfFileReader, PdfFileWriter
class PDFBookChooser:
    def __init__(self):
        self.pdf_list = []  # list to store the chosen pdf files
        pass
    def choose_file(self):
        """
        This function is used to get the file name from user input
        :return: filename (string)
        """
        try:
            file_name = input("Enter the name of your PDF file:\n")
            if not os.path.exists(file_name):
                raise FileNotFoundError("The specified file does not exist.")
            return file_name
        except Exception as e:
            print("An error occurred while getting the file name.", str(e))
