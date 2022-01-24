import numpy as np

arr = []
sum = 0
for i in range(5):
    arr.append(int(input()))
    sum += arr[i]

for i in range(5):
    if(i < len(arr)-1):
        print(arr[i], end=",")
    else:
        print(arr[i], end="\n")
print("avg: ", sum)