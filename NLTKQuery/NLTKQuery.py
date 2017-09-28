# -*- coding: utf-8 -*-
#
#
#
#

import sys
import _NLTKQuery
import _classNLTKQuery

oNLTK = _classNLTKQuery.classNTLKQuery()

print
print " 검색할 파일 또는 파일의 전체 경로 입력:"
print " 'C:/Simpson/' 등 경로에 들어갈 수 있는 문자를 입력해주세요. "
print
userSpecifiedPath = raw_input("경로 : ")

result = oNLTK.textCorpusInit(userSpecifiedPath)

if result == "성공":
    menuSelection = -1

    while menuSelection != -1:
        print
        s = raw_input('Enter키를 누르세요.')

        menuSelection = _NLTKQuery.getUserSelection()

        if menuSelection == 1:
            pass

        elif menuSelection == 2:
            pass
        elif menuSelection == 3:
            pass
        elif menuSelection == 4:
            pass
        elif menuSelection == 5:
            pass
        elif menuSelection == 6:
            pass
        elif menuSelection == 7:
            pass
        elif menuSelection == 8:
            pass
        elif menuSelection == 9:
            pass
        elif menuSelection == 10:
            pass
        elif menuSelection == 0:
            pass

        elif menuSelection == -1:
            continue

        else:
            print "오류가 발생했습니다."
            menuSelection = 0
    else:
        print "NLTK 쿼리를 종료합니다."


