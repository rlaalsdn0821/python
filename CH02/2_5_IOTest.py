"""
날짜: 2021/04/27
이름: 김철학
내용: 파이썬 표준입출력 실습 교재 p.42
"""

# 파이썬 표준 출력
print('hello', end='!')     # 자바스크립트의 document.write("hello"); 와 같은 것.
print('python')

print('010', '1234', '1111', sep='-')

# 파이썬 표준 입력
num = input('숫자 입력:')

print('입력한 숫자:', num)               #입력한 숫자: 는 사실상 '숫자'이다.
print('num result:', type(num))


# 입력받은 문자열을 숫자로 변환
result = int(num)
print('result:', result)
print('num type:', type(result))


# 서식문자 출력
print('%d년 %d월 %d일 %s요일' % (2021, 4, 27, '화'))


# 포맷문자 출력
print('이름: {}, 나이:{}, 주소:{}'.format('김유신', 23, '김해시'))
