import numpy as np

arr = []
sum = 0
for i in range(5):
    arr.append(int(input()))
    sum += arr[i]

for i in range(5):
    print(arr[i], ":  ", arr[i]**2, " ", arr[i]**0.5)