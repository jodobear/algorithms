def bubble_sort(array):
    n = len(array)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if array[j + 1] < array[j]:
                array[j + 1], array[j] = array[j], array[j + 1]
    return array

a = [1, 2, 1, 3]
print(bubble_sort(a))

def quicksort(array):
    n = len(array)
    if n <= 1:
        return array
    pivot = array.pop()

    lesser, greater = [], []

    for i in range(n - 1):
        if array[i] > pivot:
            greater.append(array[i])
        else:
            lesser.append(array[i])
    return quicksort(lesser) + [pivot] + quicksort(greater)

a = [1, 2, 1, 3]
print(quicksort(a))

def binary_search_it(sorted_array, target):
    n = len(sorted_array)
    lo = 0
    hi = n

    while(lo < hi):
        mid = lo + (hi - lo) // 2
        if target == sorted_array[mid]:
            return mid
        elif target < sorted_array[mid]:
            hi = mid - 1
        else:
            lo = mid + 1
    return -1

sa = [1, 1, 3, 4, 4, 4, 4, 5, 6]
print(binary_search_it(sa, 4))

