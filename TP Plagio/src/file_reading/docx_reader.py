import re
import sys
import docx2txt
from nltk import word_tokenize


def docx_reader(path):
    text = ''
    print(docx2txt.process(path))
    for word in word_tokenize(docx2txt.process(path)):
        text += (word + ' ') if re.search("\w", word) else ""
    return text


if __name__ == "__main__":
    if len(sys.argv) == 2:
        file_text = docx_reader(sys.argv[1])
        # Print the extracted text
        with open('file.txt', 'w') as f:
            f.write(file_text)
