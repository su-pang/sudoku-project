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

print(array)
