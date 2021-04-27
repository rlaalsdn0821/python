"""
날짜: 2021/04/26
이름: 김민우
내용: 파이썬 변수외 자료형 교제 p.38
"""

# 문자열 더하기
str1 ='Hello'
str2 ='Python'
str3 =str1+str2
print('srt3:', str3)

# 문자열 곱하기
name='홍길동'
print('name * 3:', name * 3)

# 문자열 길이(문자 갯수)
msg='Hello World'
print('msg 길이:', len(msg))   #len: 길이


# 문자열 인덱스
print('msg 1번째 문자:', msg[0])
print('msg 7번째 문자:', msg[6])
print('msg -1번째 문자:', msg[-1])
print('msg -5번째 문자:', msg[-5])


# 문자열 자르기(substring)
print('msg 0~5까지 문자열', msg[0:5])
print('msg 처음~5까지 문자열', msg[:5])      #[:5]: 처음부터 5번째까지라는 뜻, [0:5]와 같음.
print('msg 6~12까지 문자열', msg[6:11])
print('msg 6~마지막까지 문자열', msg[6:])     #[6:]: 6번째부터 마지막까지라는 뜻, [6:11]과 같음.


# 문자열 분리
people = '김유신|김춘추|장보고|강감찬|이순신'    #하나하나 분리되는 문자를 토큰이라 함. -> 토큰 5개
p1, p2, p3, p4, p5 = people.split('|')

print('p1:', p1)
print('p2:', p2)
print('p3:', p3)
print('p4:', p4)
print('p5:', p5)


people2 = '김유신^김춘추^장보고^강감찬^이순신'
p11, p22, p33, p44, p55 = people2.split('^')

print('p11:', p1)
print('p22:', p22)
print('p33:', p33)
print('p44:', p44)
print('p55:', p55)


# 문자열 이스케이프
print('서울\n대전\n대구\n부산\n광주')        # \n: 개행이라 함. (줄바꾸기)
print('서울\t대전\t대구\t부산\t광주')        # \t: tap 역할. (칸 띄우기)
print('저는 \'홍길동\' 입니다.')            # 따옴표 부분(강조부분)을 문자로 처리
print("저는 '홍길동' 입니다.")              # 이런식으로 적어도 결과가 똑같이 나옴.