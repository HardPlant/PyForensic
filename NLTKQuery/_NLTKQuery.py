# -*- coding: utf-8 -*-
#
# NLTK Query Support Method
#
#
#

def printMenu():
    print "=====NLTK 조회 옵션====="
    print "[1] 말뭉치 길이 출력"
    print "[2] 발견된 토큰 수 출력"
    print "[3] 어휘 크기 출력"
    print "[4] 정렬된 어휘 출력"
    print "[5] 연어 출력"
    print "[6] 단어 빈도 수 찾기"
    print "[7] 단어가 쓰인 문장 찾기"
    print "[8] 유사한 단어 찾기"
    print "[9] 단어 위치 찾기"
    print "[10] 어휘 출력"

    print "[0] NLTK 종료"
    print

def getUserSelection():
    printMenu()

    try:
        menuSelection = int(input('명령 입력 (0-10) >>'))
    except ValueError:
        print '입력이 잘못되었습니다. (0-10)'
        return -1

    if not menuSelection in range(0, 11):
        print '입력이 잘못되었습니다. (0-10)'
        return -1

    return menuSelection