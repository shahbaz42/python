def partition(arr, low, up):
    i = low +1
    j = up
    pivot = arr[low]
    while(i<=j):
        while(arr[i]<pivot and i<up):
            i += 1
        while(arr[j]>pivot):
            j -= 1
        if(i<j):
            (arr[i], arr[j]) = (arr[j], arr[i])
            i += 1
            j -= 1
        else :
            i += 1
    arr[low]=arr[j]
    arr[j]=pivot
    return j

arr = [13, 18, 8, 10, 21, 7, 2, 32, 6, 19]
print(partition(arr, 0, 9))
print(arr)