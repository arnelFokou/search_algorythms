📘 Search Algorithms Performance Comparison

This project compares the execution time of linear search and binary search in Python.
The goal is to highlight the differences in performance between these two search algorithms when they are applied to the same generated list.

🔍 Algorithms Implemented
1. Linear Search

Linear search scans each element of the list one by one until the target value is found.

Works on unsorted lists

Simple to implement

Slow for large datasets (O(n) time complexity)

2. Binary Search

Binary search repeatedly divides the list into halves until the target is found.

Requires the list to be sorted

Much faster on large datasets (O(log n) time complexity)

More efficient but depends on preprocessing (sorting)

🎯 Objective

The purpose of this project is to:

Measure the execution time of both search algorithms on the same dataset

Compare their performance

Demonstrate that binary search is faster, but it only works correctly on a sorted list

🧪 What the scripts do

Generate a predefined list of values

Apply linear search and measure how long it takes

Apply binary search on the sorted version of the same list

Print or plot the execution time for comparison

📈 Results (expected)

Linear search becomes slower as the list gets larger

Binary search remains very fast thanks to its logarithmic complexity

The only requirement for binary search is that the list must be sorted first

📁 Files in this repository

linear_search.py — Implementation and timing of linear search

binary_search.py — Implementation and timing of binary search

✅ Conclusion

Binary search is significantly faster than linear search, especially for large datasets, but it cannot be used unless the list is sorted.
This project illustrates how algorithmic choices impact performance in practice.
