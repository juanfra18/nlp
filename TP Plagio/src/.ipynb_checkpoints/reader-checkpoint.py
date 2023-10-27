import sys
import textract
from nltk.tokenize import word_tokenize
import first_approach


def file_reader(path):
    return str(textract.process(path).decode("utf-8"))


if __name__ == "__main__":
    if len(sys.argv) == 2:
        file_text = file_reader(f"../dataset-nlp-plagio-utn/{sys.argv[1]}")
        with open('file_reading/file.txt', 'w') as f:
            for word in first_approach.get_words(file_text):
                f.write(word+"\n")
    else:
        print("Uso: python reader.py 'nombre_del_archivo'")