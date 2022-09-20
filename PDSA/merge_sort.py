def merge(A, B):
    # let m and n represent sizes of A and B resp
    (m, n) = (len(A), len(B))

    # let C be the final array
    # let i, j, k be the pointers for A, B, C respectively.
    (C, i, j, k) = ([], 0, 0, 0)

    while k < m+n :
        # if A is empty then copy B into C and update marker
        if i == m:
            C.extend(B[j:])
            k += (n-j)

        # else if B is empty then copy A into C and update accordingly
        elif j == n :
            C.extend(A[i:])
            k += (n-i)

        # else build sorted C from A and B
        elif A[i] < B[j]:
            C.append(A[i])
            (i, k) = (i+1, k+1)
        
        else: 
            C.append(B[j])
            (j, k) = (j+1, k+1)

    return C

def merge_sort(A):
    n = len(A)

    # if length of the array is 1 ; The array is sorted return it as it is
    if n == 1 :
        return A

    # else divide the array in two equal halved left and right
    left = A[:n//2]
    right = A[n//2:]

    # sort left half and right half and return after merging both sorted arrays.
    return merge(merge_sort(left), merge_sort(right))
    
L = [int(x) for x in input().split()]
L = merge_sort(L)
print(" ".join([str(x) for x in L]))
