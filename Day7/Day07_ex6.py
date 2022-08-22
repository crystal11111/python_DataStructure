class Car:      # <자동차 만드는 설명서>
    def __init__(self, ms):     # 모든 클래스의 생성자는 __init__()
        self.maxSpeed = ms  # 객체는 반드시 생성자만을 통해서만 만든다
                            # 클래스 외부: 클래스이름()
                            # 클래스 내부: __init__()

    def info(self):
        print("최대 속력은 {}입니다.".format(self.maxSpeed))

genesis = Car(300)  # 생성자: 클래스 이름과 같은 함수
                    # 설명서를 보고 객체를 만들어 주는 함수
                    # 호출을 통해서, Car 객체를 하나 생성
genesis.info()
tico = Car(150)
tico.info()