def intersection_sorted(A, B):
    """
        This function takes two sorted arrays and returns 
        intersection of both arrays.
    """
    (m, n) = (len(A), len(B))
    (C, i, j, k) = ([], 0, 0, 0)

    while k < m+n :
        # if array A is empty 
        if i == m :
            k += (n-j)
        # if array B is empty
        elif j == n :
            k += (m-i)
        #if A[i] == B[i]
        elif A[i]==B[j]:
            C.append(A[i])
            (i, j, k) = (i+1, j+1, k+2)
        elif A[i]<B[j]:
            (i,k) = (i+1, k+1)
        else:
            (j,k) = (j+1, k+1)
    return C

L1 = [int(x) for x in input().split()]
L2 = [int(x) for x in input().split()]

R = intersection_sorted(L1, L2)

print(" ".join([str(x) for x in R]))

