from os import path
from nlp import names_in_file, process_text, distance_texts, get_title
from reader import file_reader
class TP:
    def __init__(self, nombre, posibles_profesores, text):
        self.nombre = path.basename(nombre)
        nombres = names_in_file(text)
        self.profesores = [nombre for nombre in nombres if nombre in posibles_profesores]
        self.autores = [nombre for nombre in nombres if nombre not in posibles_profesores]
        self.text = text
        for profesor in self.profesores:
            self.text = self.text.replace(profesor, "")
        for autor in self.autores:
            self.text = self.text.replace(autor, "")
        self.titulo = get_title(self.text) #Usa el texto que ya eliminó los nombres
        self.text = text.replace(self.titulo, "")

class Analysis:
    def __init__(self, tp, plagio, coincidencias): #coincidencias = [{"frase_coincidente": ...., "filename": ....}]
        self.nombre = tp.nombre
        self.titulo = tp.titulo
        self.profesores = tp.profesores
        self.autores = tp.autores
        self.plagio = plagio
        self.coincidencias = coincidencias

def comparar_archivo(path, model):
    tp = TP(path, model.profesores, process_text(file_reader(path)))
    plagio, coincidencias = calcular_plagio(tp, model)
    analisis = Analysis(tp, plagio, coincidencias)
    return analisis

def calcular_plagio(tp, model):
    distancia = 0
    descontado = 0
    coincidencias = []
    for file in model.tps:
        if file["filename"] != tp.nombre:
            d, copied = distance_texts(file["text"], tp.text)
            distancia += d
            for sent in copied:
                coincidencias.append({"frase_coincidente": sent, "filename": file["filename"]})
        else:
            descontado += 1

    return (1 - (distancia/(len(model.tps) - descontado))), coincidencias

def mostrar_data(analisis):
    print(f"Nombre del archivo: {analisis.nombre}")
    print(f"Título del trabajo: {analisis.titulo}")
    print(f"Profesores: {', '.join(analisis.profesores)}")
    print(f"Autores:  {', '.join(analisis.autores)}")
    print(f"Porcentaje de plagio: {analisis.plagio*100}%")
    if analisis.plagio > 0.5:
        conclusion = "hubo plagio"
    else:
        conclusion = "no hubo plagio"
    print(f"Conclusión: {conclusion}")
    if len(analisis.coincidencias) != 0:
        print("Coincidencias: ")
        for coincidencia in analisis.coincidencias:
            print(f"Frase: {coincidencia['frase_coincidente']}. En archivo: {coincidencia['filename']}")