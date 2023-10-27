import nltk
nltk.download('punkt')
nltk.download('stopwords')

import os
import textract
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Directory where your files are located
input_directory = '../../dataset-nlp-plagio-utn'

# Function to extract text from various file formats
def extract_text(file_path):
    try:
        text = textract.process(file_path).decode('utf-8')
        return text
    except Exception as e:
        print(f"Error extracting text from {file_path}: {e}")
        return ""

# Load stopwords and initialize the stemmer
stop_words = set(stopwords.words('spanish'))
stemmer = PorterStemmer()

# Process and vectorize the text data
texts = []
for filename in os.listdir(input_directory):
    if filename.endswith('.pdf') or filename.endswith('.docx') or filename.endswith('.doc') or filename.endswith('.pptx'):
        file_path = os.path.join(input_directory, filename)
        text = extract_text(file_path)
        texts.append(text)

# Create a TF-IDF vectorizer
tfidf_vectorizer = TfidfVectorizer()

# Transform the texts into TF-IDF vectors
tfidf_matrix = tfidf_vectorizer.fit_transform(texts)

# Calculate cosine similarity between text documents
similarity_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Print the similarity matrix
print(similarity_matrix)

# You can now analyze the similarity between the documents and detect potential plagiarism.

