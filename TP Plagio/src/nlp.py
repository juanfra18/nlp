import nltk
import nltk.metrics
import re
from nltk.tokenize import word_tokenize, sent_tokenize
nltk.download('cess_esp')
from nltk.corpus import cess_esp, stopwords
common_sentences = ["interfaces", "humanizadas", "cuatrimestre", "alumno", "legajo", "utn", "universidad", "tecnológica", "nacional", "universidad tecnológica nacional", "frba", "facultad", "regional", "buenos", "aires", "facultad regional buenos aires", "ingeniería", "en", "sistemas", "de", "información", "ingeniería en sistemas de información"]

def names_in_file(text):
    spanish_words = cess_esp.words()

    words = []
    for sentence in text.split("\n"):
        words.extend(word_tokenize(sentence))
        if sentence != "":
            words.append("\n")
    words = [word for word in words if word not in common_sentences]

    names = []
    current_name = []
    for word in words[:30]:
        processed = re.sub(r'[^A-Za-z0-9\s]', '', word.lower().strip())
        if ((len(processed) > 3 and ("." not in word)) or ((len(processed) == 1) and re.match(r'[a-z]', processed))) \
                and (not processed.isnumeric()) and \
                (processed not in spanish_words):
            current_name.append(word.lower())
        else:
            if len(current_name) > 1:
                names.append(" ".join(current_name))
            current_name = []

    return names
def get_title(text):
    for sent in get_sentences(text):
        if (sent not in common_sentences) and (not sent.replace(".", "").replace("-", "").isnumeric()):
            return sent

    return ""

def get_words(sentence):
    return [word for word in word_tokenize(sentence) if word.lower() not in stopwords.words("spanish")]

def distance_sentences(tokens1, tokens2):
    return nltk.jaccard_distance(tokens1, tokens2)

def get_sentences(text):
    sentences = []
    for sentence in text.split('\n'):
        sentences.extend(sent_tokenize(sentence))
    return sentences

def distance_texts(text1, text2):
    text1_sentences = get_sentences(text1)
    text2_sentences = get_sentences(text2)
    length = len(text2_sentences) if len(text2_sentences) < len(text1_sentences) else len(text1_sentences)
    distance = 0
    copied_sentences = []
    for i in range(length):
        set1 = set(get_words(text1_sentences[i]))
        set2 = set(get_words(text2_sentences[i]))
        d = distance_sentences(set1, set2)
        if d < 0.5: #50% de coincidencia
            copied_sentences.append((text1_sentences[i], text2_sentences[i]))
        distance += d

    return distance/length, copied_sentences
def process_text(text):
    lines = text.split('\n')  # Split the text into lines

    # Process each line separately
    processed_lines = []
    for line in lines:
        words = word_tokenize(line.lower())
        filtered_words = [word for word in words if not re.match(r'[^\w\s.]', word)]
        processed_lines.append(' '.join(filtered_words))

    # Join the processed lines back with line breaks
    processed_text = '\n'.join(processed_lines)

    return processed_text
    #return " ".join([word for word in word_tokenize(text.lower()) if not re.match(r'[^\w\s.]', word)])


if __name__=="__main__":
    print(get_title(process_text("""DOMÓTICA

Grupo 6

Pedro León

Luis Sosa

Martín Jourdan

Diego Laib

INTRODUCCIÓN

¿Que es la domótica ?

“Es la integración de la tecnología en el diseño inteligente de un recinto cerrado”

EVOLUCIÓN HISTÓRICA

1975 : Nace 

X10

Finales de los 90: Se fusionan Batibus, EIB y EHS para crear el estándar 

KNX

1999: Nace en EEUU un nuevo estándar 

Lonworks

A partir de 2006 surgen los sistemas domóticos inalámbricos RF basados en Zigbee y Zwave

El futuro : IPV6 implementado por KNX y LON

INTEGRACIÓN CON REDES

Red de control: 

Permite la conexión de los dispositivos a través de un medio físico.

Red de datos: 

Es independiente de la red de control, y permite mayor capacidad de transferencia de datos

Red multimedia: 

Es una red de alta capacidad utilizada por los dispositivos electrónicos inteligentes

Red de acceso a internet

: Permite controlar remotamente los dispositivos de un hogar.

¿QUÉ APORTA LA 

DOMÓTICA

?

La domótica contribuye a mejorar la calidad de vida del usuario.

¿QUÉ APORTA LA DOMÓTICA?

Facilitando el 

ahorro 

energético.

Fomentando la 

accesibilidad.

Aportando 

seguridad.

Convirtiendo la vivienda en un 

hogar más 

confortable.

Garantizando las 

comunicaciones.

¿QUÉ APORTA LA DOMÓTICA?

La domótica facilita la introducción de infraestructuras y la creación de escenarios que se complementan con los avances en la 

Sociedad de la Información

¿QUÉ APORTA LA DOMÓTICA?

Comunicaciones:

 Transmisión de voz y 

datos.

Mantenimiento:

 Con capacidad de incorporar el tele mantenimiento de los equipos.

Ocio y tiempo libre:

 Descansar y 

divertirse.

Salud

: Actuar en la 

sanidad.

Compra:

 Comprar y vender desde la 

casa.

Finanzas:

 Gestión del dinero y las cuentas 

bancarias.

¿QUÉ APORTA LA DOMÓTICA?

Aprendizaje:

 Aprender 

mediante los 

cursos a 

distancia.

Actividad profesional:

 Trabajar total o parcialmente desde el 

hogar.

Acceso a información:

 Museos, bibliotecas, libros, periódicos, información meteorológica, 

etc.

Ciudadanía:

 Gestiones múltiples con la Administración del 

Estado.



EMPRESAS QUE PRESTAN SERVICIOS DE DOMÓTICA



EMPRESAS QUE PRESTAN SERVICIOS DE DOMÓTICA

               Seguridad - Confort - Ahorro de energía



SEGURIDAD

Cámaras de Seguridad

Central de Alarmas

Sistemas de control de acceso

Control automático de iluminación



CONFORT

Control de iluminación

Control de artefactos eléctricos

Control de climatización



AHORRO DE ENERGÍA



Amazon Dash



Amazon Dash



Amazon Dash



Amazon Dash (Fresh)



Amazon Dash (Fresh)



Ahorro Energético

 



Estado Actual de la adopción

¿

Por 

qué estamos en esa 

Brecha?

Altos precios y altos ciclos de reemplazo

Fragmentación tecnológica

Solución a corto plazo de “ecosistemas cerrados”

Se espera que grandes de la industria se muestren como jugadores clave en el mercado.

Preocupación por privacidad y robo de datos

Intención de Compra de dispositivos

Ranking de ambientes donde 

más entusiasma 

aplicar esta tecnología

Salas de entretenimiento

Cocina""")))
