"""
날짜: 2021/04/30
이름: 김민우
내용: 파이썬 기본 입출력 하기
"""

name = input("이름을 입력하시오:")
age = input("나이를 입력하시오:")

year = 2021 - int(age)

print(name+'님은 '+age+'세이고, '+str(year)+'년도에 태어났습니다.')

n1 = int(input('첫번재 숫자: '))
n2 = int(input('두번재 숫자: '))
n3 = int(input('세번재 숫자: '))

mean =(n1 + n2 + n3) / 3

print(n1, n2, n3, "의 평균은", mean, "입니다.")