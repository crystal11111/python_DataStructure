# 입력: [2,2,3,1,3]
# 출력: [3,1,2]
# 입력: [4,2,5,5,2]
# 출력: [2,5,4]

# 방법 2.

input = [4, 2, 5, 5, 2]
      # -6 -5 -3 -2 -1
length = len(input)
output = []

index = -1
while index >= -length:
    if input[index] not in output:  # output에 input[index] 값이
        output.append(input[index])

    index -= 1

print(output)