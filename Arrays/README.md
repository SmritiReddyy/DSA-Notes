## 1. Sorting algorithms

| Algorithm | Best Case | Average Case | Worst Case | Space | Stability | Notes |
|------------|------------|---------------|-------------|---------|------------|--------|
| **Bubble Sort** | O(n) | O(n²) | O(n²) | O(1) | Stable | Repeatedly swaps adjacent elements |
| **Selection Sort** | O(n²) | O(n²) | O(n²) | O(1) | Unstable | Finds minimum each time |
| **Insertion Sort** | O(n) | O(n²) | O(n²) | O(1) | Stable | Efficient for small or nearly sorted arrays |
| **Merge Sort** | O(n log n) | O(n log n) | O(n log n) | O(n) | Stable | Divide and conquer algorithm |
| **Quick Sort** | O(n log n) | O(n log n) | O(n²) | O(log n) | Unstable | Pivot-based partitioning |
| **Heap Sort** | O(n log n) | O(n log n) | O(n log n) | O(1) | Unstable | Uses max-heap or min-heap |
| **Counting Sort** | O(n + k) | O(n + k) | O(n + k) | O(k) | Stable | Works for small range of integers |
| **Radix Sort** | O(nk) | O(nk) | O(nk) | O(n + k) | Stable | Sorts numbers digit by digit |
| **Bucket Sort** | O(n + k) | O(n + k) | O(n²) | O(n) | Stable | Works best for uniformly distributed data |

---

## 2. Searching algorithms

| Algorithm | Time Complexity | Space | Notes |
|------------|----------------|--------|--------|
| **Linear Search** | O(n) | O(1) | Sequentially checks each element |
| **Binary Search** | O(log n) | O(1) | Works only on sorted arrays |
| **Jump Search** | O(√n) | O(1) | Skips fixed steps to reduce comparisons |
| **Exponential Search** | O(log n) | O(1) | Useful when array size is unknown |

---

## 3. Common patterns and techniques

1. Two Pointer Technique  
   - Used for problems like pair sum, removing duplicates, merging sorted arrays.
2. Sliding Window Technique  
   - Used for subarray problems like max sum subarray or longest substring.
3. Prefix Sum  
   - Useful for range queries and cumulative operations.
4. Kadane’s Algorithm  
   - For finding the maximum subarray sum.
5. Binary Search on Answer  
   - Used in optimization problems (e.g., allocating pages, minimizing largest sum).

---
