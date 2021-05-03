"""
날짜: 2021/05/03
이름: 김민우
내용: 파이썬 정규표현식 교재 p.192

정규표현식(Regular Expression)
- 특정한 규칙을 갖는 문자열을 처리하기 위한 문법.
- 일반적으로 특정 문자 검색, 매치 여부를 확인할 때 정규표현식을 사용.
"""

import  re
from  re import findall, match      # findall, match 함수 선언

str1 = '1234 abc홍길동 ABC_555_6 부산광역시'

# 숫자 검색
print(findall('1234', str1))        # 1234 찾기.
print(findall('[0-9]', str1))       # 0~9까지 숫자 찾기.
print(findall('[0-9]{3}', str1))    # 0~9까지 연속 3번 나오는 숫자 찾기.
print(findall('[0-9]{3,}', str1))   # 0~9까지 연속 3자리 이상의 숫자 찾기.


# 문자열 검색
print(findall('[가-힣]{3,}', str1))       # 문자열에서 3자리 이상의 한글 찾기.
print(findall('[a-z|A-Z]{3,}', str1))    # 문자열에서 3자리 이상의 영어(소문자, 대문자) 찾기.

str2 = 'test1abcABC 123mbc 45test'
print(findall('^test', str2))       # ^: 정규표현식에서 시작을 뜻함.(test1abcABC의 test를 찾는 것이지 45text를 찾는 것이 아님) -> test로 시작하는 것을 찾는 것
print(findall('st$', str2))         # $: 정규표현식에서 피니쉬를 뜻함.


# 단어 검색
str3 = 'test^홍길동 abc 대한*민국 123$tbc'
print(findall('\\w{3,}', str3))      # \\w: 3자리 이상의 단어 찾기(특수 문자는 제외)


# 응용
jumin = '123456-1891234'
result = match('[0-9]{6}-[1-2][0-9]{6}', jumin)
# [0-9]{6}: 숫자 6자리,  [1-2][0-9]{6}: 첫번쨰[1-2](성별구분숫자), 뒤에 6자리[0-9]{6}
if result:
    print('주민번호가 맞습니다.')
else:
    print('주민번호가 아닙니다.')