import random
import time

from bubble_sort import bubble_sort
from quick_sort import quick_sort

sizes = [100, 500, 1000, 2000]
number_of_tests = 5

print("Average execution times (seconds)")

for size in sizes:
    bubble_total = 0
    quick_total = 0

    for test in range(number_of_tests):
        numbers = random.sample(range(size * 10), size)

        start = time.perf_counter()
        bubble_sort(numbers.copy())
        bubble_total += time.perf_counter() - start

        start = time.perf_counter()
        quick_sort(numbers.copy())
        quick_total += time.perf_counter() - start

    bubble_average = bubble_total / number_of_tests
    quick_average = quick_total / number_of_tests

    print("Data size:", size)
    print("Bubble Sort average:", bubble_average)
    print("Quick Sort average:", quick_average)
    print("--------------------")
