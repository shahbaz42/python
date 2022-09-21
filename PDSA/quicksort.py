import random
import time


def quicksort(L, l, r):
    """
        This recursive function takes a list and sorts recursively.
        l, r specify the section in which the quicksort performs sorting.
    """

    if r-l <= 1:
        return None

    """
    L = [ (pivot element) | lower section | upper section | unclassified section]
        * lower points to the immediate right element after the lower section 
        * upper points to the immediate right element after the upper section
    """
    
    (pivot, lower, upper) = (L[l], l+1, l+1)

    while (upper < r):
        # If L[upper] >= pivot ; increment the upper
        if L[upper] > pivot:
            upper += 1

        # swap elements at upper and lower index and increment both flags.
        else:
            (L[lower], L[upper]) = (L[upper], L[lower])
            (lower, upper) = (lower+1, upper+1)

    # move pivot to its appropriate position by swapping
    (L[l], L[lower-1]) = (L[lower-1], L[l])

    # quicksort left half
    quicksort(L, l, lower-1)
    # quicksort right half
    quicksort(L, lower, r)
    # print(l, lower, upper, r)
    return L


def analyse(sorting_algo_1, sorting_algo_2, n):
    L = [random.randint(0, n) for i in range(n)]
    t1 = time.perf_counter()
    R = sorting_algo_1(L)
    t2 = time.perf_counter()
    sorting_algo_2(L, 0, len(L))
    t3 = time.perf_counter()

    if R == L:
        print("Correct")
        print("Time taken by sorting_algo_1 : ", t2-t1)
        print("Time taken by sorting_algo_2: ", t3-t2)
    else:
        print("Incorrect")

analyse(sorted, quicksort, 10**5)