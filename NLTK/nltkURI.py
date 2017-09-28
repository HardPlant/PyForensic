import nltk
from urllib import urlopen
url = "http://www.gutenberg.org/files/2760/2760.txt"

raw = urlopen(url).read()
tokenlist = nltk.word_tokenize(raw)




