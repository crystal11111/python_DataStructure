# 입력: [2,2,3,1,3]
# 출력: [3,1,2]
# 입력: [4,2,5,5,2]
# 출력: [2,5,4]

# 방법 3.

input = [4, 2, 5, 5, 2]
input.reverse()
output = []

for i in input:
    if i not in output:
        output.append(i)

print(output)