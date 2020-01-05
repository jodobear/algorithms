# The Algorithms Meta Notes

## Bubble sort: The Compare all and swap algo

**Time:** Worst/Average: $O(n^2)$
**Space:** $O(1)$

Iterate through the whole array n times.

## Quick sort: The Pop *Pivot* algo

**Time:** Worst: $O(n^2)$ Average: $\Theta(n log n)$
**Space:** $O(n)$
Recursively pop pivot and put elements in greater/ lesser than pivot arrays.

## Binary search: The *Mid* algo

**Time:** Worst: $O(log n)$

Take mid, divide in half, check if mid >/< target, check in appropriate section and return mid if == target else return -1.

We find mid like so, `mid = lo + (hi - lo) // 2` to prevent overflow since if using unsigned int then for arrays around and bigger than $2^32 - 1$ you'll get overflow if $(hi + lo) // 2$ used even though mathematically they are same.

We assume that we have random access to the sequence. Trying to use binary search on a container such as a linked list makes little sense and it is better to use a plain linear search instead.

Binary Search can also be used for solving abstract problems using a predicate to identify the *first* of, *minimum* or the *last* of, *maximum* that resolves to the predicate. Think a sequence of yes's and no's, like so:

no, no, no, no, yes, yes, yes, yes, yes, yes

Refer to [this excellent page](https://www.topcoder.com/community/competitive-programming/tutorials/binary-search/) on topcoder for problem solving strategies using the powerful binary search.
The page is also saved [here]("./binary_search-problem_solving_strat-topcoder.md")