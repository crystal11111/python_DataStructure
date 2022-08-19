basket = ["apple", "pineapple", "banana", "orange"]

fruit = input()
basket.append(fruit)
print("바구니에 ", end= "")
for f in range(len(basket)-1):
    print("{}, ".format(basket[f]), end="")
print(basket[len(basket)-1], end="")
print("이 있습니다.")
