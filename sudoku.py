import numpy as np
import random as rd
# 함수 정의s
def new_funcrion(x, y, z):
    a = rd.randrange(1,10)
    return a

# 배열의 형태 정의
shape = (9, 3, 3)

# 배열 생성
array = np.array([[[new_funcrion(x, y, z)for z in range(shape[2])] for y in range(shape[1])] for x in range(shape[0])])

print("____________ _____________ _____________")

for i in range(array.shape[2]):
    for j in range(array.shape[1]):
        for k in range(array.shape[0]):
            if k <= 2:
                print("|", end = " ")
                print(array[k, j, i], end = " ")
        print("|", end = " ")
    print(" ")
print("____________ _____________ _____________")
for i in range(array.shape[2]):
    for j in range(array.shape[1]):
        for k in range(array.shape[0]):
            if 2 < k <= 5:
                print("|", end = " ")
                print(array[k, j, i], end = " ")
        print("|", end = " ")
    print(" ")
print("____________ _____________ _____________")
for i in range(array.shape[2]):
    for j in range(array.shape[1]):
        for k in range(array.shape[0]):
            if 5 < k <= 8:
                print("|", end = " ")
                print(array[k, j, i], end = " ")
        print("|", end = " ")
    print(" ")
print("2024.07.15")