# EX1.
# class 고양이
# method appear()

class Cat:
    count = 0
    def appear(self):
        print("고양이가 한마리 나타났습니다. 야옹!")
        Cat.count += 1
        print("지금까지 고양이는 총 {}마리 나왔습니다.".format(Cat.count))

nabi = Cat()
nabi.appear()

yaong = Cat()
yaong.appear()