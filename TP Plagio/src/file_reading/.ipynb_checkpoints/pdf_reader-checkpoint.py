import re
import sys
import pdfplumber
from nltk import word_tokenize


def pdf_reader(path):
    # Open the PDF file
    with pdfplumber.open(path) as pdf:
        text = ''
        for page in pdf.pages:
            #print(page.extract_text())
            for word in word_tokenize(page.extract_text().lower()):
                text += (word + " ") if re.search("\w", word) else "\n" if word == "\n" else ""

    return text


if __name__ == "__main__":
    if len(sys.argv) == 2:
        file_text = pdf_reader(sys.argv[1])
        # Print the extracted text
        with open('file.txt', 'w') as f:
            f.write(file_text)
