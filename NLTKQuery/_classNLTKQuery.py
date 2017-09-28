# -*- coding: utf-8 -*-

#
# NLTK QUery 클래스 모듈
#
#

import os
import sys
import logging
import nltk
from nltk.corpus import PlaintextCorpusReader

class classNTLKQuery:
    def textCorpusInit(self, thePath):
        '''

        :param thePath:
        :return:
        '''

        if not os.path.isdir(thePath):
            return "Path is not a Directory"
        if not os.access(thePath, os.R_OK):
            return "Directory is not Readable"
        try:
            self.Corpus = PlaintextCorpusReader(thePath, '.*')
            print "처리할 파일 경로: "
            print self.Corpus.fileids()
            print "기다려주세요.."

            self.rawText = self.Corpus.raw()
            self.tokens = nltk.word_tokenize(self.rawText)
            self.TextCorpus = nltk.Text(self.tokens)

        except:
            return "말뭉치 작성 실패"

        self.ActiveTextCorpus = True

        return "성공"

    def printCorpusLength(self):
        print "말뭉치 텍스트 길이:"
        print len(self.rawText)

    def printTokensFound(self):
        print "토큰의 수:"
        print len(self.tokens)

    def printVocabSize(self):
        print "계산 중..."
        print "어휘 크기:"
        vocabularyUsed = set(self.TextCorpus)
        vocabularySize = len(vocabularyUsed)
        print vocabularySize

    def printSortedVocab(self):
        print "저장된 어휘:"
        print sorted(set(self.TextCorpus))

    def printCollocation(self):
        print self.TextCorpus.collocations()

    def searchWordOccurence(self):
        myWord = raw_input("검색할 단어:")
        if myWord:
            wordCount = self.TextCorpus.coout(myWord)
            print myWord+" 발견된 수: ",
            print wordCount
        else:
            print "단어 입력이 잘못되었습니다."

    def generateConcordance(self):
        pass

    def generateSimilarities(self):
        pass

    def printWordIndex(self):
        pass

    def printVocabulary(self):
        pass


