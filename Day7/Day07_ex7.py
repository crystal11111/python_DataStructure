class Computer:
    def __init__(self, company):
        self.company = company

    def powerOn(self):
        print("{} 컴퓨터가 켜졌습니다".format(self.company))

    def powerOff(self):
        print("{} 컴퓨터가 꺼졌습니다".format(self.company))

samsung = Computer()
LG = Computer()
