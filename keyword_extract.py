import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def extrair_palavra_chave(texto):
    stop_words = set(stopwords.words('portuguese'))
    word_tokens = word_tokenize(texto)
    palavras_filtradas = [word for word in word_tokens if word.lower() not in stop_words and word.isalpha()]
    freq = nltk.FreqDist(palavras_filtradas)
    palavra_chave = freq.max()
    return palavra_chave

