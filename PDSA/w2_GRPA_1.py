import string

def combinationSort(lst):

  g = {k: [] for k in string.ascii_lowercase}

  for i in range(len(lst)):
    char=lst[i][0]
    g[char].append(lst[i])
  
  lst=[]

  for char in g.keys():
    for s in g[char]:
      lst.append(s)
  
  L1 = lst.copy() 
  i, l = 1, 0

  while i<len(lst):
    r = i
    while(r>l and lst[r][0] == lst[r-1][0] and int(lst[r-1][1:])<int(lst[r][1:])):
      lst[r], lst[r-1] = lst[r-1], lst[r]
      r -= 1
    i += 1

  return L1, lst

list = [x for x in input().split(", ")]
L1, L2 = combinationSort(list)


print("L1:", ', '.join(L1))
print("L2:", ', '.join(L2))