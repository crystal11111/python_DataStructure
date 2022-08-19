# 딕셔너리
num = {
    # key: value
    "one": 1,
    "two": 2,
    "three": 3
}
print(num)  # 딕셔너리 전체 출력
print(num["one"])   # 딕셔너리 요소 하나씩

num["three"] = 33
print(num["three"])

for key in num.keys():    # ["one", "two", "three"]
    print(key)

for value in num.values():  # [1,2,33]
    print(value)

for key, value in num.items():  # [("one" 1), ("two" 2), ("three" 3)]
    print("key:",key, " value: ", value)