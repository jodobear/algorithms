'''
# Quick Sort implementation in Python

## Keyword
Pop Pivot

## Problem Statement
Given an unsorted array of n elements, write a function to sort the array

## Approach
1. make the right-most element Pivot - pop it
2. partition the array using pivot value into two arrays
3. quicksort greater array (RHS) recursively
4. quicksort lesser array (LHS) recursively
5. return 3 & 4 concatenated with pivot array in the middle

## Time Complexity
O(n^2) worst case
O(n log n) best case
O(n log n) average case

## Space Complexity
O(log n) worst case

## Testing
For doctests run following command:
python -m doctest -v quicksort.py
or
python3 -m doctest -v quicksort.py

For manual testing run:
python3 quicksort.py

## Video Explanation
[A video explaining the Quick Sort Algorithm](https://www.youtube.com/watch?v=COk73cpQbFQ)

## Author
Tony Hoare 1959

## Algorithm Walkthrough
```
arr[] = {10, 80, 30, 90, 40, 50, 70}
Indexes:  0   1   2   3   4   5   6

low = 0, high =  6, pivot = arr[h] = 70
Initialize index of smaller element, i = -1

Traverse elements from j = low to high-1
j = 0 : Since arr[j] <= pivot, do i++ and swap(arr[i], arr[j])
i = 0
arr[] = {10, 80, 30, 90, 40, 50, 70} // No change as i and j
                                     // are same

j = 1 : Since arr[j] > pivot, do nothing
// No change in i and arr[]

j = 2 : Since arr[j] <= pivot, do i++ and swap(arr[i], arr[j])
i = 1
arr[] = {10, 30, 80, 90, 40, 50, 70} // We swap 80 and 30

j = 3 : Since arr[j] > pivot, do nothing
// No change in i and arr[]

j = 4 : Since arr[j] <= pivot, do i++ and swap(arr[i], arr[j])
i = 2
arr[] = {10, 30, 40, 90, 80, 50, 70} // 80 and 40 Swapped
j = 5 : Since arr[j] <= pivot, do i++ and swap arr[i] with arr[j]
i = 3
arr[] = {10, 30, 40, 50, 80, 90, 70} // 90 and 50 Swapped

We come out of loop because j is now equal to high-1.
Finally we place pivot at correct position by swapping
arr[i+1] and arr[high] (or pivot)
arr[] = {10, 30, 40, 50, 70, 90, 80} // 80 and 70 Swapped

Now 70 is at its correct place. All elements smaller than
70 are before it and all elements greater than 70 are after
it.
```
'''

def quicksort(array):
    '''Pure Quicksort implementation.
    Doctest:
    >>> quicksort([2, 4, 6, 8, 0, 9, 7, 5, 3, 1])
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    >>> quicksort([2, 3, 3, 1, 1, 0, 0, 0])
    [0, 0, 0, 1, 1, 2, 3, 3]
    '''
    n = len(array)
    if n <= 1:
        return array

    pivot = array.pop()  # if not popped then the array will never finish.
    greater, lesser = [], []
    for x in array:
        if x > pivot:
            greater.append(x)
        else:
            lesser.append(x)
    return quicksort(lesser) + [pivot] + quicksort(greater)

if __name__ == "__main__":
    import time

    user_input = list(map(int, input("Enter numbers separated by comma: ").split(",")))
    print("Array of numbers to sort given by user: ", user_input)
    start = time.process_time()
    print("Sorted array: ", quicksort(user_input))
    print(f"Quicksort run time: {time.process_time() - start}")