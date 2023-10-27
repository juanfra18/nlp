from src.reader import file_reader
from first_approach import distance_texts, get_sentences

if __name__ == "__main__":
    print(distance_texts(
        get_sentences(file_reader("../dataset-nlp-plagio-utn/tpN5 hERNAN.doc")),
        get_sentences(file_reader("../dataset-nlp-plagio-utn/TP1.docx"))
    ))
    #print(get_sentences(file_reader("../dataset-nlp-plagio-utn/tpN5 hERNAN.doc")))
    #print(get_sentences(file_reader("../dataset-nlp-plagio-utn/TP1.docx")))
    """get_sentences(file_reader("../dataset-nlp-plagio-utn/tpN5 hERNAN.doc")),
        file_reader("../dataset-nlp-plagio-utn/tpN5 hERNAN.doc")"""