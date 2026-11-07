# Algorithm Analysis and Implementation

## 1. Introduction
Sorting algorithms are used to arrange data in a specific order, for example from the smallest number to the largest number. In this task, I selected Bubble Sort and Quick Sort because they both solve the same problem but use different methods. I wanted to understand how these methods affect performance when the number of items increases.

## 2. Implementation
Both algorithms were implemented using Python. Bubble Sort compares two neighbouring numbers and changes their positions when they are in the wrong order. Quick Sort uses a pivot to divide the numbers into smaller groups. In my implementation, the first number is selected as the pivot. The algorithm then sorts the smaller and larger groups using recursion.

## 3. Performance Analysis
I tested both algorithms with four different data sizes: 100, 500, 1,000 and 2,000 items. Each test was repeated five times, and I calculated the average execution time.
The results showed that Quick Sort was faster than Bubble Sort in all tests. For 2,000 items, Bubble Sort took approximately 0.200689 seconds, while Quick Sort took approximately 0.001978 seconds.
For smaller data sets, such as 100 items, the difference in execution time was relatively small. However, as the data size increased, Bubble Sort became much slower. Quick Sort handled the larger data sets more efficiently in my tests.
Bubble Sort has an average and worst-case time complexity of O(n²). Quick Sort has an average time complexity of O(n log n), but its worst-case complexity is O(n²) because it uses the first item as the pivot. These results show how the choice of algorithm can affect performance when working with larger amounts of data.

## 4. Conclusion
This experiment helped me understand the relationship between algorithms and performance. Quick Sort was more efficient in my tests, especially with larger data sets. Bubble Sort is still useful for learning basic sorting concepts, but Quick Sort can be a better choice for larger collections under average conditions.
Sorting algorithms can also be used in real-world applications. For example, an online shopping website may use sorting algorithms to arrange products by price, from lowest to highest. This makes it easier for customers to find the products they want. This task helped me understand why choosing the right algorithm is important when developing software.
