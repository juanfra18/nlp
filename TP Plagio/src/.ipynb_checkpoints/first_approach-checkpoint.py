import nltk.metrics #https://www.nltk.org/_modules/nltk/metrics/distance.html
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords

def get_sentences():
    sentence1 = input("First sentence: ")
    sentence2 = input("Second sentence: ")
    return sentence1, sentence2

# Tokenize sentences and remove stopword
def get_words(sentence):
    return [word for word in word_tokenize(sentence) if word.lower() not in stopwords.words("spanish")]

def get_sentences(text):
    return sent_tokenize(text);

# Calculate Jaccard similarity
def distance_sentences(tokens1, tokens2):
    return nltk.jaccard_distance(tokens1, tokens2)

def distance_texts(text1_sentences, text2_sentences):
    length = len(text2_sentences) if len(text2_sentences) < len(text1_sentences) else len(text1_sentences)
    distance = 0
    for i in range(length):
        set1 = set(get_words(text1_sentences[i]))
        set2 = set(get_words(text2_sentences[i]))
        d = distance_sentences(set1, set2)
        distance += d

    return distance
    #return sum(distance_sentences(set(get_words(text1_sentences[i])), set(get_words(text1_sentences[i]))) for i in range(length))/length


if __name__ == "__main__":
    sentence1, sentence2 = get_sentences()
    print("Jaccard Similarity:", distance_sentences(get_words(sentence1), get_words(sentence2)))

