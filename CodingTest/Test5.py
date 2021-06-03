"""
날짜: 2021/06/03
이름: 김민우
내용: 코딩 테스트 - 시각
"""

h = int(input())

count = 0

for i in range(h+1):
    for j in range(60):
        for k in range(60):

            if '3' in str(i) + str(j) +str(k):
                count += 1

print(count)

