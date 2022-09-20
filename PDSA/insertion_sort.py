def insertion_sort(L):
    """
        Iterative Insertion sort
    """
    n = len(L)
    if n<1:
        return(L)

    for i in range(n):
        # Assume L[:i] is sorted
        # Move L[i] to correct position in L[:i]
        j = i
        while (j>0 and L[j]<L[j-1]):
            L[j-1], L[j] = L[j], L[j-1]
            j = j-1
        # Now L[:i+1] is sorted
    return(L)

L = [int(x) for x in input().split()]
L = insertion_sort(L)
print(" ".join([str(x) for x in L]))

# import random
# L = [random.randint(0, 1000) for i in range(100000)]
# print(" ".join([str(x) for x in L ]))