"""
날짜: 2021/05/03
이름: 김민우
내용: 파이썬 외부 패키지 입출력 실습 교재 p.239
"""

# 파이참 하단 -> Terminal 클릭 -> pip3 install openpyxl 입력 -> 엔터
from  openpyxl import Workbook      # 엑셀 파일 사용 가능.import

# Excel 파일 쓰기


# 엑셀 파일 객체 생성
workbook = Workbook()


# 활성화된 sheet 선택
sheet = workbook.active


# 데이터 입력
sheet['A1'] = '홍길동'     # A1: A열 1번째행.
sheet.append([1, 2, 3])
sheet.append(['김유신', '김춘추', '장보고'])
sheet.cell(6, 2, '사과')      # 2열 6행에 사과 입력.


# 엑셀 파일 저장/닫기
workbook.save('C:/Users/bigdata/Desktop/Sample.xlsx')
workbook.close