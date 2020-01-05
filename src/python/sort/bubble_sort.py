'''
# Bubble Sort implementation in Python

## Keyword
Compare all and swap

## Problem Statement:
Given an unsorted array of n elements, write a function to sort the array

## Approach:
1. Start from the beginning, compare two adjacent indexes; i & j s.t. i < j. If element at i > element at j then swap them else do nothing.
2. Do step 1 for all the indexes and n times on the array.

## Time Complexity:
O(n^2) - worst case
O(n) - best case
O(n^2) - average case

## Space Complexity:
O(1) - worst case

## Testing
For doctests run:
python -m doctest -v bubble_sort.py
or
python3 -m doctest -v bubble_sort.py

For manual test run:
python3 bubble_sort.py

## Video Explanation
[A video explaining the Bubble Sort Algorithm](https://www.youtube.com/watch?v=Jdtq5uKz-w4)

## Algorithm Walkthrough
```
arr[] = {10, 80, 40, 30}
Indexes: 0   1   2   3

1. Index = 0, Number = 10
2. 10 < 80, do nothing and continue

3. Index = 1, Number = 80
4. 80 > 40, swap 80 and 40
5. The array now is {10, 40, 80, 30}

6. Index = 2, Number = 80
7. 80 > 30, swap 80 and 30
8. The array now is {10, 40, 30, 80}

	Repeat the Above Steps again

arr[] = {10, 40, 30, 80}
Indexes: 0   1   2   3

1. Index = 0, Number = 10
2. 10 < 40, do nothing and continue

3. Index = 1, Number = 40
4. 40 > 30, swap 40 and 30
5. The array now is {10, 30, 40, 80}

6. Index = 2, Number = 40
7. 40 < 80, do nothing
8. The array now is {10, 30, 40, 80}

	Repeat the Above Steps again

arr[] = {10, 30, 40, 80}
Indexes: 0   1   2   3

1. Index = 0, Number = 10
2. 10 < 30, do nothing and continue

3. Index = 1, Number = 30
4. 30 < 40, do nothing and continue

5. Index = 2, Number = 40
6. 40 < 80, do nothing

Since there are no swaps in above steps, it means the array is sorted and we can stop here.
```
'''

def bubble_sort(array):
    '''Pure Bubble Sort implementation
    Doctest:
    >>> bubble_sort([2, 4, 3, 5, 1])
    [1, 2, 3, 4, 5]
    '''

    n = len(array)
    if n <= 1:
        return array

    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):  # Every iteration of i we reduce the length of our run since the last element is always sorted.
            swapped = True
            if array[j] > array[j + 1]:
                swapped = True
                array[j], array[j + 1] = array[j + 1], array[j]
            # Stop iteration if we don't swap - array is sorted.
            if not swapped:
                break
    return array

if __name__ == "__main__":
    import time

    user_input = list(map(int, input("Enter numbers separated by comma: ").split(",")))
    print("Array of numbers to sort given by user: ", user_input)
    start = time.process_time()
    print("Sorted array: ", bubble_sort(user_input))
    print(f"Bubble sort run time: {time.process_time() - start}")