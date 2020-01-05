'''
# Various Binary Search implementations in Python

### Keyword
The Mid
### Problem Statement
Given a sorted  array of n elements, write a function to search for the index of a given element (target)

### Approach
1. Divide the array in half - repeatedly.
2. Take the middle element. Set lo = 0 and hi = len(array) - 1
3. If mid < target then search in RHS of mid (lo = middle + 1, hi = len(array))
4. Else if middle > target then search in LHS of mid (lo = 0, hi = middle - 1)
5. Else if mid == target return mid
5. Else return -1 if element not found i.e. lo > hi (base case).

### Time Complexity
O(log n) worst case
O(1) best case

### Space Complexity
O(1) for iterative approach
O(log n) for recursive approach due to recursion call stack

### Testing
For doctests run following command:
python -m doctest -v binary_search.py
or
python3 -m doctest -v binary_search.py

For manual testing run:
python3 binary_search.py

#### Video Explanation
[CS50 video explaining the Binary Search Algorithm](https://www.youtube.com/watch?v=5xlIPT1FRcA)
'''

def binary_search_it(sorted_array, target):
    '''Pure iterative implementation of binary search
    Doctests:
    >>> binary_search_it([1, 2, 3, 4, 5], 4)
    3
    >>> binary_search_it([1, 2, 3, 4, 5], 6)
    -1
    '''
    lo = 0
    hi = len(sorted_array) - 1

    while(lo < hi):
        mid = lo + (hi - lo) // 2  # good practice, more robust - to prevent overflow
        if sorted_array[mid] == target:
            return mid
        elif sorted_array[mid] > target:
            hi = mid - 1
        else:
            lo = mid + 1
    return -1

# print(binary_search_it([1, 2, 3, 4, 5], 6))

def binary_search_rec(sorted_array, target, lo, hi):
    """Recursive implementation of Binary search
    Start the recursion with lo = 0 & hi = len(sorted_array) - 1
    Doctests:
    >>> binary_search_rec([1, 2, 3, 4, 5], 4, 0, len([1, 2, 3, 4, 5]) - 1)
    3
    >>> binary_search_rec([1, 2, 3, 4, 5], 6, 0, len([1, 2, 3, 4, 5]) - 1)
    -1
    """
    if lo > hi:
        return -1

    mid = lo + (hi - lo) // 2

    if sorted_array[mid] == target:
        return mid
    elif sorted_array[mid] > target:
        return binary_search_rec(sorted_array, target, lo, mid - 1)
    else:
        return binary_search_rec(sorted_array, target, mid + 1, hi)


def binary_search_std_lib(sorted_array, target):
    '''Std lib implementation of Binary Search
    Doctests:
    >>> binary_search_it([1, 2, 3, 4, 5], 4)
    3
    >>> binary_search_it([1, 2, 3, 4, 5], 6)
    -1
    '''
    import bisect

    index = bisect.bisect_left(sorted_array, target)
    # 1st check if you haven't reached end of array
    # 2nd check if elem at index == target
    if index != len(sorted_array) and sorted_array[index] == target:
        return index
    return -1

def __assert_sorted(array):
    """Check if passed array is sorted else raise ValueError.
    Doctest:
    >>> __assert_sorted([0, 1, 2, 3, 4])
    True
    >>> __assert_sorted([0, 1, 3, 2, 4])
    Traceback (most recent call last):
    ...
    ValueError: Array must be sorted in ascending order
    """
    if array != sorted(array):
        raise ValueError("Array must be sorted in ascending order")
    return True

if __name__ == "__main__":
    import time, sys

    user_input = list(map(int, input("Enter numbers in ascending order separated by comma:\n").split(",")))
    try:
        __assert_sorted(user_input)
    except ValueError:
        sys.exit("Numbers must be in ascending order to apply binary search")

    target = int(input("Enter a single number you want to find in the sequence:\n"))
    it_result = binary_search_it(user_input, target)
    rec_result = binary_search_rec(user_input, target, 0, len(user_input) - 1)
    std_lib_result = binary_search_std_lib(user_input, target)

    if it_result != -1:
        print(f"Iterative binary search found the target; {target} at position: {it_result}")
    else:
        print(f"Iterative binary search says target; {target} not found in the provided sequence.")
    if rec_result != -1:
        print(f"Recursive binary search found the target; {target} at position: {rec_result}")
    else:
        print(f"Recursive binary search target; {target} not found in the provided sequence.")
    if std_lib_result != -1:
        print(f"Standard library binary search found the target; {target} at position: {std_lib_result}")
    else:
        print(f"Standard library binary search says target; {target} not found in the provided sequence.")
