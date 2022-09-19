def findLargest(L):
  l = 0
  s = len(L)
  r = s-1
  temp = []

  if (s<2):
    return L[0]
    
  while (l<=r):
    m=(l+r)//2
    temp.append(L[m])
    if (m == s-1):
      nxt = 0
    else:
      nxt = m+1

    if (L[m] > L[nxt]):
      return L[m]
    elif (L[m] < L[0]):
      r = m-1
    else:
      l = m+1
#   print(temp)
    


lst = [int(x) for x in input().split(" ")]
print(findLargest(lst))