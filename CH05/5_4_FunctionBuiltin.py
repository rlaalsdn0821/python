"""
날짜: 2021/04/29
이름: 김민우
내용: 파이썬 내장함수 교재 p.118
"""

# 수학관련
import math        # 모듈선언
import random      # 모듈선언
import time        # 모듈선언


# 절대값
r1 = abs(-5)     # abs: 절잿값을 반환하는 함수
print('r1:', r1)


# 올림
r2 = math.ceil(1.2)       # ceil: 올림
r3 = math.ceil(1.8)
print('r2:', r2)
print('r3:', r3)


# 내림
r4 = math.floor(1.2)       # floor: 내림
r5 = math.floor(1.8)
print('r4:', r4)
print('r5:', r5)


# 반올림
r6 = round(1.2)     # round: 반올림
r7 = round(1.8)
print('r6:', r6)
print('r7:', r7)


# 제곱근
r8 = math.sqrt(4)
r9 = math.sqrt(9)
print('r8:', r8)
print('r9:', r9)


# random
num1 = random.random()
print('num1:', num1)  # 0~1 사이의 실수

num2 = num1 * 10      # 10 미만으로 값이 나옴.
print('num2:', num2)  # 0~10 사이의 실수

num3 = math.ceil(num2)
print('num3:', num3)  # 1~10 사이의 정수

num4 = math.ceil(random.random() * 10)             # num1, num2, num3 코드를 중첩한 형태.
print('num4:', num4)  # 1~10 사이의 정수


# 날짜, 시간
t1 = time.time()      # 유닉스 타임: 1970년 1월 1일 기준으로 시작된 시간.
print('t1:', t1)

t2 = time.ctime()     # 변환된 유닉스 타임
print('t2:', t2)

now = time.localtime(time.time())
year = time.strftime('%Y', now)
month = time.strftime('%m', now)
date = time.strftime('%d', now)
hour = time.strftime('%H', now)
min = time.strftime('%M', now)
sec = time.strftime('%S', now)

print('%s년 %s월 %s일' % (year, month, date))
print('%s시 %s분 %s초' % (hour, min, sec))