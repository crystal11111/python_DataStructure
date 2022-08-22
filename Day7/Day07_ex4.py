# 클래스 예제
class Barista:
    # 생성자
    def __init__(self, name):     # 개발자가 직접 생성자를 구현
        self.name = name          # 자바: this.name = name

    def hello(self):
        print("어서오세요. 저는 바리스타 {}입니다.".format(self.name))

    def serve(self):
        print("커피나왔습니다.")

barista = Barista("ssong")     # 생성자 호출 --> 객체가 변수를 갖고 태어남
"""
    생성자: 클래스와 이름이 같은 특별한 함수
    기능 -> 클래스를 보고 객체 생성
           객체 생성 빼고 딱히 할 일이 없으면, 개발자가 구현 안하고 생략되어있음

"""
barista.hello()
barista.serve()