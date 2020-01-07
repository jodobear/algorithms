'''Implementation of some basic math problems in python.'''

import math

def prime_factors(n: int) -> list:
    '''Prime Factorization of an integer using sieve.

    The Algorithm:
    First we deal with all the composite numbers in 1 then then prime numbers in 2.
    1.  Evens by checking n % 2 == 0 and then do n / 2 to reduce n for each 2.
    2. Prime numbers starting from 3 until √n since any 2 numbers > √n, s.t. a * b > n and hence can't be a factor of n.
    In step 2 of the above algorithm, we run a loop and do following in loop
        a) Find the least prime factor i (must be less than √n,)
        b) Remove all occurrences i from n by repeatedly dividing n by i.
        c) Repeat steps a and b for divided n and i = i + 2. The steps a and b are repeated till n becomes either 1 or a prime number.

    Time Complexity: O(log n)

    Doctest:
    >>> prime_factors(100)
    [2, 2, 5, 5]
    >>> prime_factors(510)
    [2, 3, 5, 17]
    '''
    # NOTE: the int()s are important otherwise you get floats.

    pf = []
    # first deal with all the evens
    while n % 2 == 0:
        pf.append(2)
        n = int(n / 2)
    # then all the rest
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            pf.append(i)
            n = int(n / i)
    # n will either be 1 or a prime number
    if n > 2:
        pf.append(n)
    return pf


def number_of_divisors(n: int) -> int:
    '''Get a list of number of divisors of an integer.

    We use similar technique as to find prime factors.
    We add two variables div & temp and do the following:
    1. For each even factor we find we increment temp & reduce n / 2.
    2. Once completely reduced, we multiply it to div, meaning that many times we could reduce n / 2 i.e. as many divisors exist for n.
    3. Then similar to step 2 of prime_factors we check for prime numbers and do following in loop up to sqroot of remaining n:
        a. We reset temp and for each i (3, √n + 1, 2) while n % i == 0, we reduce n / i and increment temp
        c. Once completely reduced i.e. n = 1, we multiply temp to div, i.e. as many times as you could reduce n / 2, you can achieve n with all the i's * those even divisors.

    Time Complexity: O(log n)

    Doctest:
    >>> number_of_divisors(100)
    9
    '''
    div = 1
    temp = 1
    while n % 2 == 0:
        temp += 1
        n = int(n / 2)
        print(n)
    div *= temp
    print('div after evens: ', div)
    print(n)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        temp = 1
        while n % i == 0:
            print('i: ', i)
            temp += 1
            n = int(n / i)
        print('temp after while: ', temp)
        div *= temp
    return div

# def list_all_divisors(n: int) -> list:

# def sum_of_all_divisors(n: int) -> int: