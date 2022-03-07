import random
import time
"""
This program is for Fun!
"""

tup_list = [1,(2,3),4,5,6,(7,8)]

def is_sorted(list):
    """
    checks if a hybrid list with int and tuples datatypes
    is sorted
    """
    sorted = True
    for i in range(len(list)-1):
        e1 = list[i]
        e2 = list[i+1]

        if type(e1) == tuple:
            e1 = e1[1]
        if type(e2) == tuple:
            e2 = e2[1]

        if e1 >= e2 :
            sorted = False
            break
    return sorted

def bogosort(list):
    """
    bogosort.
    """
    count = 0
    while sorted(list) != list:
        count += 1
        random.shuffle(list)
        print(count, list)

def bogosort_PRO_MAX_ULTRA(list):
    """
    Bogosort PRO MAX ULTRA
    """
    count = 0
    while is_sorted(list) == False :
        random.shuffle(list)
        count += 1
        print(count,list)
        for i in range(0,len(list)-1,2):
            e1 = list[i]
            e2 = list[i+1]
            if (type(e1)==int and type(e2)==int) and e2-e1 == 1 and ((e1, e2) not in list): 
                print(e1, e2)
                list.append((e1,e2))
                list.remove(e1)
                list.remove(e2)
                break

    new_list = []

    for i in list:
        if type(i) == int :
            new_list.append(i)
        else:
            new_list.append(i[0])
            new_list.append(i[1])

    return new_list
    
list = [14,13,12,11,10,9,8,7,6,5,4,3,2,1]
print(bogosort_PRO_MAX_ULTRA(list))

print("\n Now sorting same list with regular bogosort in 3,2,1")
time.sleep(5)

list = [14,13,12,11,10,9,8,7,6,5,4,3,2,1]
print(bogosort(list))
