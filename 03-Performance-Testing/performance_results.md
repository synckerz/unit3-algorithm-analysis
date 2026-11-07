# Performance Test Results

## Test Environment

The tests were performed on the student's personal computer using Python 3.13.14.

- Processor architecture: AMD64
- Operating environment: Windows
- Python version: 3.13.14

## Performance Measurements

Each data size was tested five times. The average execution time was calculated for both algorithms.

| Data size | Bubble Sort average (seconds) | Quick Sort average (seconds) |
|---:|---:|---:|
| 100 | 0.000418800 | 0.000229700 |
| 500 | 0.009870580 | 0.000471000 |
| 1,000 | 0.043605400 | 0.001031060 |
| 2,000 | 0.200689480 | 0.001978140 |

## Observations

The results show that Quick Sort was faster than Bubble Sort at all four data sizes in this experiment.

The difference became more noticeable as the data size increased. For 2,000 elements, Bubble Sort took approximately 0.200689 seconds, while Quick Sort took approximately 0.001978 seconds.

These measurements depend on the computer and test run, so small differences may occur when the test is repeated. Each repetition creates a random list and passes a copy of the same list to both algorithms.

The results provide practical evidence of the difference between the average time complexities of Bubble Sort (O(n²)) and Quick Sort (O(n log n)).