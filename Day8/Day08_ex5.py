class Snack:

    company = "롯대"

    def __init__(self, n, p):
        self.name = n
        self.price = p

    def info(self):
        print("{}는 {}원이고, 제조회사는 {}입니다".format(self.name, self.price, Snack.company))

pepero = Snack("빼빼로", 1500)
potatochip = Snack("포테토칩", 1800)
pepero.info()
potatochip.info()

Snack.company = "오리온"
pepero.info()
potatochip.info()