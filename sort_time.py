from selectionSort import *
from bubbleSort import *
from insertionSort import *
from mergeSort import *
import random
import time
import sys
import matplotlib.pyplot as plt

sys.setrecursionlimit(1000000)
listLength = 300

sum = 0

B = []
for value in range(0, listLength):
    B.append(random.randint(0, 100))

for value in range(0, 1000):
    A = B
    start = time.time()
    bubbleSortRec(A, listLength)
    end = time.time()
    sum += end - start

print("bub:", sum / 1000)
    

for value in range(0, 1000):
    A = B
    start = time.time()
    selectionSortRec(A, listLength)
    end = time.time()
    sum += end - start

print("sel:", sum / 1000)

for value in range(0, 1000):
    A = B
    start = time.time()
    insertionSortRec(A, 0, listLength)
    end = time.time()
    sum += end - start

print("ins:", sum / 1000)

for value in range(0, 1000):
    A = B
    start = time.time()
    mergeSortRec(A)
    end = time.time()
    sum += end - start

print("mer:", sum / 1000)

plt.figure(figsize=(10, 6))
for i, algorithm in enumerate(algorithms):
    plt.plot(sizes, times[i], label=algorithm)

plt.xlabel("Input Size")
plt.ylabel("Execution Time (seconds)")
plt.legend()
plt.title("Sorting Algorithm Comparison")
plt.grid(True)
plt.show()
