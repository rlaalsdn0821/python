"""
날짜: 2021/05/03
이름: 김민우
내용: 파이썬 파일 입출력 실습 교재 p.217
"""

# 파일 읽기(File Input)
file1 = open('C:/Users/bigdata/Desktop/Sample.txt', 'r')        # r: read 모드
line = file1.readline()

print('line:', line)
file1.close()


# 여러줄 파일 읽기
file2 = open('C:/Users/bigdata/Desktop/Sample.txt', 'r')

while True:
    line = file2.read()

    if not line:
        # 읽을 라인이 없을 경우
        break

    print(line)

file2.close()


# 파일 쓰기(File Output)
file3 = open('C:/Users/bigdata/Desktop/Test.txt', 'w')      # w: write 모드
# Test.txt: 파일이 없으므로 바탕화면에 가상파일로 만들어짐.
file3.write('안녕하세요.\n')
file3.write('반갑습니요.\n')
file3.write('감사합니다.\n')
file3.close()


# 구구단 쓰기
file4 = open('C:/Users/bigdata/Desktop/gugudan.txt', 'w')

for x in range(2, 10):

    file4.write('%d단\n' % x)

    for y in range(1, 10):
        z = x * y
        file4.write('{} x {} = {}\n'.format(x, y, z))

file4.close()