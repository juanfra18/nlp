import os
import textract
from reader import file_reader
from nlp import process_text

class Dataset:
    def __init__(self, path):
        self.files = []
        for file in os.listdir(path):
            try:
                self.files.append({'filename': file, 'text': file_reader(path+"/"+file)})
            except: #quizás hacer que el file_reader levante una excepcion propia
                pass

class Model:
    def __init__(self, dataset):
        self.profesores = ["alejandro prince", "emilio borré", "emilio borre"]
        self.get_tps(dataset)

    def get_tps(self, dataset):
        self.tps = [{'filename': file["filename"], 'text': process_text(file["text"])} for file in dataset.files]

def train_model(path):
    dataset = Dataset(path)
    return Model(dataset)
#asumir que el TP tiene el título bien
#chequear tema minúsculas/mayúsculas