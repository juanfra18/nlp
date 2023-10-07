import nltk.metrics #https://www.nltk.org/_modules/nltk/metrics/distance.html
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def get_sentences():
    sentence1 = input("First sentence: ")
    sentence2 = input("Second sentence: ")
    return sentence1, sentence2

# Tokenize sentences and remove stopword
def get_tokens(sentence):
    return set(word_tokenize(sentence.lower())) - set(stopwords.words("english"))

# Calculate Jaccard similarity
def calculate_distance(tokens1, tokens2):
    return 1 - nltk.jaccard_distance(tokens1, tokens2)

if __name__ == "__main__":
    sentence1, sentence2 = get_sentences()
    print("Jaccard Similarity:", calculate_distance(get_tokens(sentence1), get_tokens(sentence2)))

