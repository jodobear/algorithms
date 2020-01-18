'''
# Merge Sort implementation in Python

## Keyword
Merge Partitions

## Proplem Statement
Given an unsorted array of n elements, write a function to sort the array

## Approach
Recursively partition the array into two parts and then join from the bottom comparing the elements, placing them in the correct order.

## Time Complexity
Worst - O(log n)
Best -
Average -

## Space Complexity

## Testing
For doctests run:
python -m doctest -v bubble_sort.py
or
python3 -m doctest -v bubble_sort.py

For manual test run:
python3 bubble_sort.py

'''

def mergesort_rec(a):
    '''
    Recursive implementation of Merge Sort: given an array, returns the same sorted ascending.

    Doctests:
    >>> merge_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]

    >>> merge_sort([])
    []

    >>> merge_sort([-2, -5, -45])
    [-45, -5, -2]
    '''
    def merge(lhs, rhs):
        ''' merge individual elements - the smallest unit.
        The return will concatenate whatever's left, either lhs or rhs.'''
        result = []
        while lhs and rhs:
            result.append((lhs if lhs[0] <= rhs[0] else rhs).pop(0))
        return result + lhs + rhs

    if len(a) <= 1:
        return a
    mid = len(a) // 2
    return merge(mergesort_rec(a[:mid]), mergesort_rec(a[mid:]))

a = [2, 1, 3, 4, 7, 6, 5]
print(mergesort_rec(a))

def mergesort_it(a):
    '''next time'''