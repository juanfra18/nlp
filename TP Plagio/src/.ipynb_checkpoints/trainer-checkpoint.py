import os
import textract
from reader import file_reader
from nlp import names_in_file, get_titles
from first_approach import get_words

class Dataset:
    def __init__(self, path):
        self.files = []
        for file in os.listdir(path):
            try:
                self.files.append({'filename': file, 'text': file_reader(path+"/"+file)})
            except textract.exceptions.ShellError: #quizás hacer que el file_reader levante una excepcion propia
                pass

class Model:
    def __init__(self, dataset):
        self.get_profesores(dataset)
        self.get_titulos(dataset)
        self.tps = self.get_tps(dataset)

    def get_profesores(self, dataset):
        #obtener nombres de los textos, y añadir los que se repiten en más de 10
        self.profesores = []
        contador_nombres = {}
        for file in dataset.files:
            nombres = names_in_file(file['text'])
            for nombre in nombres:
                if nombre in contador_nombres:
                    contador_nombres[nombre] += 1
                else:
                    contador_nombres[nombre] = 1

        for nombre in contador_nombres:
            if contador_nombres[nombre] > 10:
                self.profesores.append(nombre)

    def get_titulos(self, dataset):
        self.titulos = []
        posibles_titulos = []
        #Procesar el texto para sacar las palabras y normalizarlo
        texts = [get_words(text) for text in dataset.files["text"]]
        for i in range(len(texts)):
            aux = ""
            for word in texts[i]:
                aux += word.upper() + " "
            texts[i] = aux



#asumir que el TP tiene el título bien
#chequear tema minúsculas/mayúsculas
class TP:
    def __init__(self, nombre, posibles_titulos, posibles_profesores, text):
        self.nombre = nombre
        self.titulo = [titulo for titulo in posibles_titulos if titulo in text][0]
        nombres = names_in_file(text)
        self.profesores = nombres in posibles_profesores
        self.autores = nombres not in posibles_profesores
        self.text = text.replace(self.titulo, "")
        for profesor in self.profesores:
            self.text = self.text.replace(profesor, "")
        for autor in self.autores:
            self.text = self.text.replace(autor, "")

if __name__=="__main__":
    data = Dataset("../dataset-nlp-plagio-utn")
    for file in data.files:
        print(file["filename"])