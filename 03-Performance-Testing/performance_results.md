# Performance Test Results

## Test Environment

The tests were performed on the student's personal computer.

- Operating system: Windows
- Processor architecture: AMD64
- Python version: 3.13.14

## Performance Measurements

Each data size was tested five times. The average execution time was calculated for both algorithms. Separate copies of the same randomly generated list were used to ensure a fair comparison.

| Data size | Bubble Sort average (seconds) | Quick Sort average (seconds) |
|---:|---:|---:|
| 100 | 0.000356960 | 0.000088880 |
| 500 | 0.008776560 | 0.000640700 |
| 1,000 | 0.046256400 | 0.001107720 |
| 2,000 | 0.193783160 | 0.001949280 |

## Observations

The results show that Quick Sort was faster than Bubble Sort at all four data sizes in this experiment.

The performance difference became more noticeable as the data size increased. For 2,000 elements, Bubble Sort took approximately 0.193783 seconds, while Quick Sort took approximately 0.001949 seconds.

This means that Quick Sort was approximately 99.4 times faster than Bubble Sort for the largest data set tested.

Bubble Sort has an average and worst-case time complexity of O(n²). Quick Sort has an average time complexity of O(n log n), although its worst-case complexity is O(n²) because the first element is selected as the pivot.

The measurements may vary between test runs depending on the computer and execution environment. These results represent the averages obtained during this particular experiment.
