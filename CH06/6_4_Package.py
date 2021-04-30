"""
날짜: 2021/04/30
이름: 김민우
내용: 파이썬 패키지와 모듈 실습하기 교재 p.175
"""

import CH06.sub2.calc  # 출처 선언
import CH06.sub2.calc as c  # 출처 선언,    as c: import 선언에 대한 별칭을 c로 지음.
from CH06.sub2.calc import *  # 출처 선언

r1 = CH06.sub2.calc.plus(1, 2)
r2 = c.minus(2, 3)
r3 = multi(3, 4)
r4 = div(4, 2)

print('r1:', r1)
print('r2:', r2)
print('r3:', r3)
print('r4:', r4)