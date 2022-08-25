# 상속 (Inheritance) self-study
# only for 객체지향언어
# 자식 클래스가 부모 클래스에게 뭔가를 받을 때

# Super Class
class Pet():
    species = '종'
    colour = '색깔'
    food = '주 음식'

    def tell(self):
        print("동물의 특징!")

# Sub Class
class Cat(Pet):
    def __init__(self, n):
        self.name = n

    def cry(self):
        print("{}는 야옹 울어요".format(self.name))


