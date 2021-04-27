"""
날짜: 2021/04/27
이름: 김철학
내용: 파이썬 자료구조 리스트 실습 교재 p.84
"""

# 리스트 생성
list1 = [1, 2, 3, 4, 5]          # 인덱스번호: [0] [1] [2] [3] [4]

print('list1 type:', type(list1))
print('list1[0]:', list1[0])
print('list1[2]:', list1[2])
print('list1[3]:', list1[3])


list2 = [5, 3.14, True, 'Apple']

print('list2 type:', type(list2))
print('list2[1]:', list2[1])
print('list2[2]:', list2[2])
print('list2[3]:', list2[3])


list3 = [[1,2,3],
         [4,5,6],
         [7,8,9]]

print('list3 type:', type(list3))
print('list3[0][0]', list3[0][0])        #1행 1열
print('list3[1][1]', list3[1][1])        #2행 2열
print('list3[2][1]', list3[2][1])        #3행 2열


# 리스트 덧셈
animal1 = ['사자', '호랑이', '코끼리']
animal2 = ['곰', '기린']

result = animal1 + animal2
print('result:', result)


# 리스트 수정, 추가, 삭제
nums = [1, 2, 3, 4, 5]
print('nums:', nums)

nums[1] = 7          # 수정
print('nums:', nums)

nums[2:4] = [8, 9, 10]           # 추가
print('nums:', nums)

nums[3:5] =[]               # 삭제
print('nums:', nums)


