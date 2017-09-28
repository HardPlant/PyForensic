#-*- coding: utf-8 -*-
from __future__ import division
import nltk
from nltk.corpus import PlaintextCorpusReader # Corpus => 말뭉치
nltk.download('punkt')

rootOfCorpus = 'e://simpson//'

newCorpus = PlaintextCorpusReader(rootOfCorpus, '.*')
print type(newCorpus)

print newCorpus.fileids()
print newCorpus.abspaths()

rawText = newCorpus.raw()
print len(rawText)

tokens = nltk.word_tokenize(rawText)
print len(tokens)
print tokens[0:100]
