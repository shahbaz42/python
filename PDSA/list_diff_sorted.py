def list_diif(A,B):
    """
    this function takes two sorted lists A and B and 
    returns a list of all elements that are present in A but
    not in B
    """
    (m, n) = (len(A), len(B))
    (C, i, j, k) = ([], 0, 0, 0)

    while k < m+n :
        # A is empty then increment j and k suitably to end the loop
        if i==m:
            k += (n-j)

        # B is empty copy all elements of A in C
        elif j==n :
            C.extend(A[i:])
            k +=  (m-i)

        # if A[i] < B[j] then Append A[i] to C
        elif A[i] < B[j] :
            C.append(A[i])
            (i, k) = (i+1, k+1)
        
        # if A[i] > B[j] then increment flag of B until 
        # B[j] becomes either equal to A[i]
        # or greater than A[i]; 
        elif A[i] > B[j] :
            (j, k) = (j+1, k+1)
        
        # if A[i] == B[j] increment both flags
        # and increment K twice.
        else :
            (i, j, k) = (i+1, j+1, k+2)

    return C

L1 = [int(x) for x in input().split()]
L2 = [int(x) for x in input().split()]

R = list_diif(L1, L2)

print(" ".join([str(x) for x in R]))



