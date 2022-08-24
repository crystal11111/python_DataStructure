# 튜플
L = [1, 2, 3, 4, 5]     # list
l2 = [6, 7, 8]
l3 = []
l4 = [13]

T = (1, 2, 3, 4, 5)     # tuple
t2 = (6, 7, 8)
t3 = ()
t4 = (13, )     # 튜플로 한개 생성 할 때 (,)붙혀야 함


# 전체출력
print(L)
print(T)

# 부분 출력(slicing)
print(L[1:4])   # 1번자리~3번자리
print(T[1:4])

# 요소출력
print(L[2])
print(T[2])

# 통째로 추가하는 건 됨
L = L + l2
T = T + t2
print(L)
print(T)

# 값 중간에 바꾸는 거 튜플 안됨
L[2] = 10
print(L)
# T[2] = 10

# 값 삭제하는 거 튜플 안됨
del L[0]
print(L)
# del T[0]