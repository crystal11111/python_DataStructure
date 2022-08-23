# Ex.01 class player
# 함수 - play() : "000 선수 (00세) 경기에 출전합니다."
# 생성자: 이름, 나이

class Player:
    def __init__(self, n, a):
        self.name = n
        self.age = a

    def play(self):
       print("{}선수 ({}세) 경기에 출전합니다.".format(self.name, self.age))


sonny = Player("손흥민", 30)       #self 생략되어있음
sonny.play()    # 손흥민 선수 (30세) 경기에 출전합니다.