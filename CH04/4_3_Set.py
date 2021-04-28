"""
날짜: 2021/04/27
이름: 김민우
내용: 파이썬 자료구조 Set 실습 교재 p.96
"""

# Set 생성(순서, 순복 없음)
set1 = {1, 2, 3, 4, 5, 3}            # Set: 집합 -> 5개 (3은 중복이므로 6개가 아님)
print('set1 type:', type(set1))
print('set1:', set1)


set2 = set('Hello World')
print('set2 type:', type(set2))
print('set2:', set2)                # 문자 순서가 랜덤으로 나옴


# 집합 출력(List 변환)
list1 = list(set1)
print('list1:', list1)
print('list1[0]:', list1[0])
print('list1[3]:', list1[3])

list2 = list(set2)
print('list2:', list2)
print('list2[0]:', list2[0])
print('list2[3]:', list2[3])