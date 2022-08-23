class Family:

    address = ""    # 클래스 변수 선언

    def __init__(self, n, a):   # 생성자 = constructor
        self.name = n
        Family.address = a  # 클래스.변수 = 값

    def info(self):
        print("저는 {}이구요, {}에 살고 있어요".format(self.name, Family.address))

    def move(self, new):
        Family.address = new
    
dad = Family("아빠", "서울")
dad.info()

son = Family("아들", "서울")
son.info()

dad.move("부산")
dad.info()
son.info()      # 클래스 변수로 값이 바뀜