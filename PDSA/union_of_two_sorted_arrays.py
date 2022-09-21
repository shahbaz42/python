def union_sorted(A,B):
    (m, n) = (len(A), len(B))
    (C, i, j, k) = ([], 0, 0, 0)

    while (k < m+n ):
        # check if A is empty
        if i == m :
            C.extend(B[j:])
            k += (n-j)
        # check if B is empty
        elif j == n :
            C.extend(A[i:])
            k += (m-i)
        # if top most elements  of both arrays are equal then 
        # print append one ; increment both pointers and
        # increment k twice
        elif A[i]==B[j]:
            C.append(A[i])
            (i, j, k) = (i+1, j+1, k+2)

        elif A[i]<B[j]:
            C.append(A[i])
            (i, k) = (i+1, k+1)
        else:
            C.append(B[j])
            (j, k) = (j+1, k+1)
    
    return C

L1 = [int(x) for x in input().split()]
L2 = [int(x) for x in input().split()]

R = union_sorted(L1, L2)

print(" ".join([str(x) for x in R]))
