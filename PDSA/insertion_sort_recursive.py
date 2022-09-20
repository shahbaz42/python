def insert(sorted_L, v):
    """
        This function inserts a value at its appropriate position in a sorted array.
    """
    n = len(sorted_L)
    # if length is 0 then simply return a singleton
    if n == 0 :
        return([v])
    
    #if last element of sorted_L is less than v then append at last and return
    if sorted_L[-1] <= v :
        sorted_L.append(v)
        return sorted_L

    # insert v in an array without last element 
    arr =  insert(sorted_L[:-1],v)

    # do append the last element of the array before returning.
    arr.append(sorted_L[-1])

    return arr

def insertion_sort_recursive(L):
    """
        This function sorts a list using recursive insertion sort.
    """
    n = len(L)
    # if length of the list is 0 then return the list
    if n < 1 :
        return L
    
    # we know that insertion_sort_recursive will return sorted list
    # and insert function will take a sorted list and an elemen and insert it to its appropriate place
    # we can recursively divide the array into and array of [n-1 elements], and sort the array of [n-1 elements]
    # using insertion sort and insert last element using insert function.
    return insert(insertion_sort_recursive(L[:-1]),L[-1])

L = [int(x) for x in input().split()]
L = insertion_sort_recursive(L)
print(" ".join([str(x) for x in L]))