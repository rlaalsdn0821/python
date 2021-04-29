"""
날짜: 2021/04/29
이름: 김민우
내용: 파이썬 클래스 실습하기 교재 p.148
"""

# 클래스 정의
class Account:
    # 클래스는 보통 대문자로 정의.
    # 클래스는 속성과 기능으로 정의됨.
    # 속성
    def __init__(self, bank, id, name, money):    # 매개 변수도 넣어야 함.
        self.bank = bank     # 값 초기화
        self.id = id         # 값 초기화
        self.name = name       # 값 초기화
        self.money =money      # 값 초기화
        # 필드 4개

    # 기능
    def deposit(self, money):
        self.money += money     # 입금한 금액만큼 계좌에 돈을 더함.

    def withdraw(self, money):
        self.money -= money     # 출금한 금액만큼 계좌에서 돈을 뺌.

    def show(self):
        print('--------------')
        print('은행명:', self.bank)
        print('계좌번호:', self.id)
        print('입금주:', self.name)
        print('현재잔액:', self.money)
        # 현실에 가지고 있는 계좌의 기능을 정의함.
