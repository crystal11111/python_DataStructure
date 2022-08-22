# 딕셔너리 예제
# 가위바위보

win = {"가위": "바위",
        "바위": "보",
        "보": "가위"
       }

while True:
    user1 = input()
    user2 = input()

    # if user1 or user2 == "그만"  X -->   조건 자리에 1개만 들어가면, 그 변수에 값이 0이 아니면 다 참
    if user1 == "그만" or user2 == "그만":
        print("게임을 종료하겠습니다")
        break

    if user2 == win[user1]:
        print("와! 이겼다!")
    elif user1 == win[user2]:
        print("아이고 졌다!")
    else:
        print("비겼다")