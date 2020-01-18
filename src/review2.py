'''Review 2 20-01-18'''

def bubble_sort(a):
    n = len(a)
    for i in range(n - 1):
        for j in range(i + 1, n - 1):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
    return a

a = [1, 2, 3, 5, 6, 1, 2, 2, 4]
print(bubble_sort(a))
'''All good'''

def quicksort(a):
    n = len(a)
    if n <= 1:
        return a
    pivot = a.pop(-1)
    lhs, rhs = [], []
    for i in a:
        if i < pivot:
            lhs.append(i)
        else:
            rhs.append(i)
    return quicksort(lhs) + [pivot] + quicksort(rhs)

a = [1, 2, 3, 5, 6, 1, 2, 2, 4]
print(quicksort(a))
''' I've started using JS syntax in python, used push instead of append (lol!).. had to read the algo steps to remember the return statement. Got confused as to how to return.'''

def is_sorted(a):
    if a == sorted(a):
        return True
    raise ValueError("The array is not sorted")
'''refreshed how to raise an error.'''

def bin_search_it(a, q):
    ''' Discrete case. for continuous: hi = mid & lo = mid'''
    import sys
    try:
        is_sorted(a)
    except ValueError:
        sys.exit("The array is not sorted.")
    lo = 0
    hi = len(a) - 1

    while lo < hi:
        mid = lo + (hi - lo) // 2
        if a[mid] == q:
            return mid
        elif a[mid] > q:
            hi = mid - 1
        else:
            lo = mid + 1
    return -1
'''refreshed the try..except syntax. this was clear.'''

a = [1, 2, 1, 2, 2, 3, 4, 5, 6]
print(bin_search_it(a, 5))

def bin_search_rec(a, q, lo, hi):
    if lo > hi:
        return -1
    mid = lo + (hi - lo) // 2
    if a[mid] == q:
        return mid
    elif a[mid] > q:
        return bin_search_rec(a, q, lo, mid - 1)
    else:
        return bin_search_rec(a, q, mid + 1, hi)
    return -1
'''here i started with while, which is ok except if you init with hi = len(a) - 1 then you need to use the check lo >= hi else it won't check the last elem.'''

a = [1, 1, 2, 2, 2, 3, 4, 5, 6]
print(bin_search_rec(a, 6, 0, len(a) - 1))

def bin_search_std_lib(a, q):
    import bisect
    index = bisect.bisect_left(a, q)
    if index != len(a) and a[index] == q:
        return index
    return -1
'''basically looked up and wrote again for repetition'''

a = [1, 1, 2, 2, 2, 3, 4, 5, 6]
print(bin_search_std_lib(a, 6))

def primeFactors(n):
    import math

    pf = [1, ]
    while n % 2 == 0:
        pf.append(2)
        n = int(n / 2)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            pf.append(i)
            n = int(n / i)
        if n > 1:
            pf.append(n)
    return pf

print(primeFactors(36))
'''
Had to read the algo steps and tried to reproduce but, couldn't successively.
1. the loops are not just one time checks. You want to reduce as long as you can.
2. forgot to implement the sqrt. Also, note the + 1, without it doesn't work since the range isn't inclusive so you end up with n - 1 not n.
'''

def noOfDivisors(n):
    import math

    div = 1
    count = 1
    while n % 2 == 0:
        count += 1
        n = int(n / 2)
    div *= count
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        count = 1
        while n % i == 0:
            count += 1
            n = int(n / i)
        div *= count
    return div

print(noOfDivisors(100))
'''
Read the algo steps and still wasn't able to write a completely correct implementation.
The idea is simple, find as many prime factors and each time you find a particular type of factor, like 2(even) or 3s or 5s, etc. you increment the count and multiply it to the div.
Note, the count init is 1 and that after each type of div, we reset the count.

I understand this algo a lot better now.
'''
