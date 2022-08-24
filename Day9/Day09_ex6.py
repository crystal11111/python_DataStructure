# 입력: [2,2,3,1,3]
# 출력: [2,1,1,1]
# 입력: [7,8,8,9]
# 출력: [1,2,1]

input = [7, 8, 8, 9]
count = 0
length = len(input)

for i in range(length):
    count += 1
    if input[i] == input[i+1]:
        count += 1

print(list(count))