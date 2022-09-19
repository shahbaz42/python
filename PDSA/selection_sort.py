def selection_sort(L):
    """Sort a list of items in ascending order"""

    n = len(L)

    for i in range(n):
        # i = {0,1,2,3,4}
        index = i

        for j in range(i, n):
            # j = {1,2,3,4}
            if L[j] < L[index]:
                index = j

        #swap ith position with minimum
        (L[i], L[index]) = (L[index], L[i])  

    return L

L = [int(x) for x in input().split()]
L = selection_sort(L)

print(" ".join([str(x) for x in L]))
            

