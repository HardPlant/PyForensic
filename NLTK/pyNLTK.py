#-*- coding: utf-8 -*-
from __future__ import division
import nltk
from nltk.corpus import PlaintextCorpusReader # Corpus => 말뭉치
rootOfCorpus = 'e://simpson//'

newCorpus = PlaintextCorpusReader(rootOfCorpus, '.*')
print type(newCorpus)

