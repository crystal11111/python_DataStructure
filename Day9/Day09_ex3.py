# 알고리즘 문제
# 입력: [2,2,3,1,3]
# 출력: [3,1,2]
# 입력: [4,2,5,5,2]
# 출력: [2,5,4]

# 방법 1.

input = [2, 2, 3, 1, 3]
output = []
length = len(input)     # **해결법**

index = 0
while index < length:       # index < 5: 0, 1, 2, 3, 4
    # 0 < 5
    # 1 < 4
    # 2 < 3
    # 3 < 2     X -> ()튜플로 바꾸기

    result = input.pop()          # pop() 1) 리스트 끝 요소를 제거
    if result in output:          #       2) 뭘 제거 했는지 알려줌
        pass
    else:
        output.append(result)
    index += 1

print(output)
