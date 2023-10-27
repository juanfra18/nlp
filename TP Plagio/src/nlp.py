import nltk
import nltk.metrics
import re
from nltk.tokenize import word_tokenize, sent_tokenize
nltk.download('cess_esp')
from nltk.corpus import cess_esp, stopwords
COMMON_STRINGS = ["cátedra", "interfaces", "humanizadas", "cuatrimestre", "alumno", "legajo", "utn", "universidad", "tecnológica", "nacional", "universidad tecnológica nacional", "frba", "facultad", "regional", "buenos", "aires", "facultad regional buenos aires", "ingeniería", "en", "sistemas", "de", "información", "ingeniería en sistemas de información"]

def names_in_file(text):
    spanish_words = cess_esp.words()
    N = 50

    words = []
    for sentence in text.split("\n"):
        words.extend(get_words(sentence))
        if sentence != "":
            words.append("\n")
    words = [word for word in words[:N] if (word not in COMMON_STRINGS and (word not in spanish_words))]

    names = []
    current_name = []
    for word in words:
        processed = re.sub(r'[^\w\s]', '', word.lower().strip())
        if ((len(processed) > 3 and ("." not in word)) or ((len(processed) == 1) and re.match(r'[a-z]', processed))) \
                and (not processed.isnumeric()):
            current_name.append(word.lower().strip())
        else:
            if len(current_name) > 1:
                names.append(" ".join(current_name))
            current_name = []

    return names
def get_title(text):
    for sent in get_sentences(text):
        if (sent not in COMMON_STRINGS) and (not sent.replace(".", "").replace("-", "").isnumeric()):
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
    lines = text.split('\n')

    processed_lines = []
    for line in lines:
        words = word_tokenize(line.lower())
        filtered_words = [word for word in words if (not re.match(r'[^\w\s.]', word)) or (word == "\xad")]
        processed_lines.append(' '.join(filtered_words))

    processed_text = '\n'.join(processed_lines)

    return processed_text
