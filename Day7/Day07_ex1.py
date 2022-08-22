# 알고리즘 문제
# 입력: [2,2,3,1,3]
# 출력: [3,1,2]
# 입력: [4,2,5,5,2]
# 출력: [2,5,4]

num = [2, 2, 3, 1, 3]
r_num = list(reversed(num))

for i in r_num:
    for j in r_num:
        if i == j:
           r_num.remove(i)
print(r_num)