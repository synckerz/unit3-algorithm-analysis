# Unit 3 – Algorithm Analysis and Implementation

This project contains introductory Python implementations of Bubble Sort and Quick Sort, a small performance experiment, recorded results, a performance graph, an analysis report, and a learning reflection.

## Contents

- `01-Introduction/algorithm_notes.md` – Basic algorithm and complexity notes.
- `02-Python-Implementation/bubble_sort.py` – Bubble Sort implementation.
- `02-Python-Implementation/quick_sort.py` – Quick Sort implementation.
- `02-Python-Implementation/performance_test.py` – Five-run average timing test.
- `03-Performance-Testing/performance_results.md` – Measured performance results.
- `03-Performance-Testing/performance_graph.png` – Performance comparison graph.
- `04-Analysis-Report/analysis_report.md` – Completed analysis report.
- `04-Analysis-Report/report_planning.md` – Report planning notes.
- `05-Reflection/learning_reflection.md` – Completed learning reflection.
- `05-Reflection/reflection_prompts.md` – Reflection guidance questions.

## Run the Performance Test

The three Python files are located in the `02-Python-Implementation` folder.

Open a terminal in that folder and run:

python performance_test.py


The test compares Bubble Sort and Quick Sort using four different data sizes: 100, 500, 1,000 and 2,000 items.

Each data size is tested five times, and the average execution time is calculated.

The recorded timings may vary depending on the computer and test run. The results table and graph use the five-run averages recorded during the experiment.

## Implementation Notes

### Bubble Sort

Bubble Sort uses nested loops without an early-stop feature. It compares neighbouring values and swaps them when they are in the wrong order.

Its best, average and worst-case time complexities are O(n²). It sorts the list in place and uses a temporary variable to swap neighbouring values.

### Quick Sort

This Quick Sort implementation uses the first item as its pivot and creates three lists: `smaller`, `equal` and `larger`.

Its average time complexity is O(n log n), while its worst-case time complexity is O(n²) when pivot choices are unfavourable.

This is a simple learning implementation and is not production-optimised.

## Project Completion

The Python implementations, performance experiment, recorded results, graph, analysis report and learning reflection are included in this e-portfolio.

The project demonstrates the differences between two sorting algorithms and how algorithm choice can affect software performance, especially when working with larger amounts of data.