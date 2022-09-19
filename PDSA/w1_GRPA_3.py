def odd_one(L):
    dtype_array = []
    count = {}
    answer = ""
    for i in L :
        dtype_array.append(type(i).__name__)

    for i in dtype_array:
        if i in count.keys():
            count[i] += 1
        else :
            count[i] = 1
    
    for i in count.keys():
        if count[i] == 1 :
            answer = i
    
    return answer




print(odd_one(eval(input().strip())))