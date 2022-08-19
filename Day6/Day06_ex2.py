bread = ["초코롤", "소라빵"]

while True:
    print("행동을 선택하세요. 1.고객이 빵을 산다 2.진열대를 확인한다 3.고객이 집에 갑니다")
    option = int(input())

    if option == 1:
        print("고객이 "+ bread.pop() +"을 구매했습니다")

    if option == 2:
        print("진열대에는 ", end="")
        print(bread, end="")
        print("가 있습니다.")
        if len(bread) <= 3:
            bread.append("식빵")
            print("진열대에 빵이 3개 이하라서, 식빵을 1개 추가했습니다.")
            print("진열대에는 ", end="")
            print(bread, end="")
            print("가 있습니다.")

    if option == 3:
        print("고객이 집에 갔습니다.")
        break