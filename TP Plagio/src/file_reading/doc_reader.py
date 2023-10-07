import os
import shutil
import sys
from src.file_reading import docx_reader

def doc_reader(path):
    shutil.copy(path, "output.doc")
    os.rename("output.doc", "output.docx")
    text = docx_reader.docx_reader("output.docx")
    os.remove("output.docx")
    return text


if __name__ == "__main__":
    if len(sys.argv) == 2:
        file_text = doc_reader(sys.argv[1])
        # Print the extracted text
        with open('file.txt', 'w') as f:
            f.write(file_text)