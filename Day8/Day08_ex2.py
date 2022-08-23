"""
자바: 객체를 가지고 프로그래밍하는 언어
    = 객체 지향 프로그래밍
    = Object-Oriented Programming(OOP)
    클래스, 객체, 함수, 변수, 생성자,....

파이썬: OOP
"""
class Member:

    total_count = 0
    # 생성자
    def __init__(self, n, c):
        self.name = n
        self.count = c

    # 메소드: 클래스 내부 함수
    def enter(self):    # self <-- 호출 한 객체가 들어감
        print("{} 회원이 입장하였습니다".format(self.name))
        self.count += 1
        Member.total_count += 1
        print("{}님 입장 횟수: {}회".format(self.name, self.count))
        print("오늘 총 입장 횟수는 {}회".format(Member.total_count))
        print()

kelly = Member("켈리", 0)
kelly.enter()
kelly.enter()

tom = Member("톰", 0)
tom.enter()
tom.enter()

# 객체(instance) 변수
# self.변수: 객체 변수
#         : 각 객체가 가지는 그 객체의 속성을 나타낼때
#           ex) 나이, 이름, ...
