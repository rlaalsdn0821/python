"""
날짜: 2021/05/13
이름: 김민우
내용: 코딩 테스트 - 큰 수의 법칙
"""

# n, m, k를 공백으로 구분하여 입력받기
# n: 배열 크기, m: 전체 덧셈 횟수, k: 반복 횟수
n, m, k = map(int, input().split())

# n개의 숫자를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

# 리스트를 내림차순으로 정렬
data.sort(reverse=True)

# 첫번재로 큰 수
first = data[0]

# 두번째로 큰 수
second = data[1]

result = 0

repeat = k

for i in range(m):

    if repeat > 0:
        result += first
        repeat -= 1
    else:
        result += second
        repeat = k

print(result)