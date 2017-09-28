#-*- coding: utf-8 -*-
from __future__ import division
import nltk
from nltk.corpus import PlaintextCorpusReader # Corpus => 말뭉치
nltk.download('punkt')
nltk.download('stopwords')

rootOfCorpus = 'e://simpson//'

newCorpus = PlaintextCorpusReader(rootOfCorpus, '.*')
rawText = newCorpus.raw()
tokens = nltk.word_tokenize(rawText)
textSimpson = nltk.Text(tokens)
vocabularyUsed = set(textSimpson)
myWord = "KILL"

print textSimpson.collocations()