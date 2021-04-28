"""
날짜: 2021/04/27
이름: 김민우
내용: 파이썬 조건문 if 실습 교재 p.60
"""

# if
num1, num2 = 1, 2

if num1 > 0:
    print('num1은 0보다 크다.')

if num1 > num2:
    print('num1은 num2보다 크다.')

if num1 > 0:
    if num2 > 1:
      print('num1은 0보다 크고 num2는 1보다 크다.')

if num1 > 0 and num2 >1:
    print('num1은 0보다 크고 num2는 1보다 크다.')

# if ~ else
num3, num4 = 3, 4

if num3 > num4:
    # 조건이 참일 때
        print('num3이 num4보다 크다.')
else:
        # 조건이 거짓일 때
        print('num3이 num4보다 작다.')


# if ~ elif ~ else
if num1 > num2:
    print('num1은 num2보다 크다.')
elif num2 > num3:
    print('num2은 num3보다 크다.')
elif num3 > num4:
    print('num3은 num4보다 크다.')
else:
    print('num4가 가장 크다.')


# 상향 조건문
num = 3
result = num * 2 if num >= 5 else num + 2
# num이 3보다 크거나 작으면 num*2, 그렇지 않으면 num+2
print('result:', result)


# 확인문제
score = int(input('점수 입력:'))
print('점수 확인:', score)

if score >=90 and score <= 100:
    print('A 입니다.')
elif score >=80 and score < 90:
    print('B 입니다.')
elif 70 <= score < 80:
    print('C 입니다.')
elif 60 <= score < 70:
    print('D 입니다.')
elif score < 60:
    print('F 입니다.')


#if score가 90점 이상 100점 이하이면:
    #rint('A 입니다.')
#elif score가 80점 이상 89점 이하이면:
    #print('B 입니다.')
#elif score가 70점 이상 79점 이하이면:
    #print('C 입니다.')
#elif score가 60점 이상 69점 이하이면:
    #print('D 입니다.')
#elif score가 60점 미만:
    #print('F 입니다.')
