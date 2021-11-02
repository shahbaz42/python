import random
import time

def check_distinct_obvious(L):
    """
    obvious way of checking if a list has all distinct element.
    returns 1 if all elements are distinct, else returns 0. 
    """
    flag =  1
    for i in range(len(L)-1):
        for j in range(i+1, len(L)):
            # in case you see two elements being the same, declare non-distinct
            if L[i] == L[j] :
                flag = 0
    return flag


def create_movie_theater(n):
    """
    simply create a theater with n slots
    """
    H = []
    for i in range(n):
        H.append([])
    
    return H

def put_element(x, H):
    """
    x is a person with an aadhar number and we look at last
    two digits and we assign him a seat in the theator.
    """
    H[x%len(H)].append(x)
    return H

def present_or_not(x, V):
    """
    x is an element, V is a list, it will just check linearly
    if x is present in V or not.
    """
    if x in V :
        return 1
    
    else :
        return 0


def distinct_genius(L):
    """
    The central idea is , We take every single element of the list,
    we push the element to the appropreate seat in the theator. as we 
    push we check if the element is present in vertical seats or not.
    """

    H = create_movie_theater(len(L))
    flag = 1
    for i in range(len(L)):
        seat_number = L[i]%len(L)
        if present_or_not(L[i] , H[seat_number]):
            flag = 0
        H[seat_number].append(L[i])
    
    return flag


n = 50000
l = []


for i in range(n):
    l.append(random.randint(1, n))

t1 = time.time()
print(distinct_genius(l))
t2 = time.time()

print("Time taken by genius method : ", t2-t1, " sec")

t1 = time.time()
print(check_distinct_obvious(l))
t2 = time.time()

print("Time taken by obvious method :", t2-t1, " sec")