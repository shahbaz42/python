def mergeInPlace(A, B):
    m = len(A)
    n = len(B)
    if (m < 1 or n < 1):
        return

    for i in range(0, m):
        if (A[i] > B[0]):
            A[i], B[0] = B[0], A[i]

        j = 0
        while (j < n - 1 and B[j] > B[j + 1]):
            B[j], B[j + 1] = B[j + 1], B[j]
            j += 1


a1 = [int(x) for x in input().split()]
a2 = [int(x) for x in input().split()]

mergeInPlace(a1, a2)

print(" ".join([str(x) for x in a1]))
print(" ".join([str(x) for x in a2]))
