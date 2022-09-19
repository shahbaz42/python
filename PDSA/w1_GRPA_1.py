def find_Min_Difference(L,P):

    if len(L) < 1 :
        return 0

    L.sort()
    min_diff = L[-1]-L[0]
    # print(L)
    for i in range(0, len(L)-P):
        temp = L[i+P-1] - L[i]
        # print(f"{L[i+P-1]}- {L[i]} = {temp}")
        if temp < min_diff : 
            min_diff = temp

    return(min_diff)

L=eval(input().strip())
P=int(input())
print(find_Min_Difference(L,P))