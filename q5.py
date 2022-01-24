import random
import numpy as np

random_array = random.sample(range(-100, 100), 7)
print("1x: ")
for i in range(len(random_array)):
    print(random_array[i], end=" ")

print("\n2x: ")
for i in range(len(random_array)):
    print(random_array[i] * 2, end=" ")