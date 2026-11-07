# Algorithm notes

A sorting algorithm puts data into an order, such as smallest to largest.

- **Bubble Sort:** compares neighbouring values. If the left value is larger, it swaps the two values. Repeated passes move larger values towards the end.
- **Quick Sort:** chooses a pivot and separates values into groups smaller than, equal to, and larger than the pivot. It then sorts the smaller groups.

## Complexity terms
- `n` means the number of items.
- **Average case** means expected performance across typical inputs.
- **Worst case** means performance in the least favourable input situation.
- Big-O describes how the amount of work grows as input size increases; it is not a time measurement in seconds.

For the implementations in this portfolio:
- Bubble Sort: average O(n²), worst O(n²).
- Quick Sort: average O(n log n), worst O(n²), because this version always chooses the first item as pivot.
