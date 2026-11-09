# Algorithm Analysis and Implementation

## 1. Introduction

Sorting algorithms are important in software development because they organise data into a specific order. In this project, I implemented Bubble Sort and Quick Sort using Python. Both algorithms solve the same sorting problem, but they use different approaches. The purpose of this experiment was to compare their performance and understand how algorithm efficiency changes as the amount of data increases.

## 2. Implementation

Bubble Sort compares adjacent elements and swaps them when they are in the wrong order. It repeatedly passes through the list until the elements are arranged in ascending order.

Quick Sort uses the divide-and-conquer approach. In my implementation, the first element is selected as the pivot. The remaining elements are divided into three groups: smaller, equal and larger. The smaller and larger groups are then sorted recursively.

## 3. Performance Analysis

Both algorithms were tested using four different data sizes: 100, 500, 1,000 and 2,000 elements. Each test was repeated five times, and the average execution time was calculated.

The same randomly generated data was provided to both algorithms during each repetition. Separate copies were created before timing to avoid including list-copying time in the measurements.

The results were:

| Data size | Bubble Sort (seconds) | Quick Sort (seconds) |
|---:|---:|---:|
| 100 | 0.000356960 | 0.000088880 |
| 500 | 0.008776560 | 0.000640700 |
| 1,000 | 0.046256400 | 0.001107720 |
| 2,000 | 0.193783160 | 0.001949280 |

Quick Sort was faster than Bubble Sort at every tested data size. For 2,000 elements, Quick Sort was approximately 99.4 times faster.

Bubble Sort has an average and worst-case time complexity of O(n²). Quick Sort has an average time complexity of O(n log n), although its worst-case complexity is O(n²). This can happen when the selected pivot repeatedly produces unbalanced partitions.

The experimental results support the theoretical expectation that Quick Sort generally performs better on larger data sets. However, these measurements represent one computer and one experimental environment, so they should not be treated as universal execution times.

## 4. Algorithm Comparison and Selection

Bubble Sort is relatively simple to understand and implement. It is useful for learning basic sorting principles, but its quadratic time complexity makes it less suitable for larger data sets.

Quick Sort is more complex because it uses recursion and partitioning. However, its average time complexity makes it a more efficient choice for larger collections.

Based on the theoretical analysis and the experimental results, I would select Quick Sort for this particular implementation when working with larger data sets. Bubble Sort remains useful for educational purposes and understanding algorithm fundamentals.

## 5. Conclusion

This project helped me understand how algorithm design influences software performance. Implementing and testing two sorting algorithms showed me that different approaches to the same problem can produce significantly different execution times.

I also learned the importance of designing fair performance experiments, using repeated measurements and comparing practical results with theoretical time complexity.

Sorting is relevant to real-world software systems, including e-commerce applications where products may need to be arranged by price, rating or popularity. Choosing an appropriate algorithm can help improve the efficiency and responsiveness of such systems.
