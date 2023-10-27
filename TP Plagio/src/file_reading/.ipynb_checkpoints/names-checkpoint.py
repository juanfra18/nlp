import nltk

from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree

text = '''
Hola, mi nombre es Juan F. Paoli. Me gusta jugar a la pelota.
Sé hablar español, inglés, griego y latín.
'''

with open("file.txt","r") as f:
    text = f.read()

nltk_results = ne_chunk(pos_tag(word_tokenize(text)))
for nltk_result in nltk_results:
    if type(nltk_result) == Tree:
        name = ''
        for nltk_result_leaf in nltk_result.leaves():
            name += nltk_result_leaf[0] + ' '
        print ('Type: ', nltk_result.label(), 'Name: ', name)