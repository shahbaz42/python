def insertion_sort(L):
    """
        Iterative Insertion sort
    """
    n = len(L)

    for i in range(n):
        j = i
        while (j>0 and L[j]<L[j-1]):
            L[j-1], L[j] = L[j], L[j-1]
            j = j-1
            
    return(L)

L = [int(x) for x in input().split()]
L = insertion_sort(L)
print(" ".join([str(x) for x in L]))

# import random
# L = [random.randint(0, 1000) for i in range(100000)]
# print(" ".join([str(x) for x in L ]))