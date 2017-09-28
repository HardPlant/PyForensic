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


