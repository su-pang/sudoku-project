
import numpy as np


array = np.arange(1, 82).reshape(9, 3, 3)


print("_______________ _______________ _______________")

for i in range(array.shape[2]):
    for j in range(array.shape[1]):
        for k in range(array.shape[0]):
            if k <= 2:
                print("|", end = " ")
                print(array[k, j, i], end = " ")
        print("|", end = " ")
    print(" ")
print("_______________ _________________ ________________")
for i in range(array.shape[2]):
    for j in range(array.shape[1]):
        for k in range(array.shape[0]):
            if 2 < k <= 5:
                print("|", end = " ")
                print(array[k, j, i], end = " ")
        print("|", end = " ")
    print(" ")
print("_______________ _________________ ________________")
for i in range(array.shape[2]):
    for j in range(array.shape[1]):
        for k in range(array.shape[0]):
            if 5 < k <= 8:
                print("|", end = " ")
                print(array[k, j, i], end = " ")
        print("|", end = " ")
    print(" ")

