def neighbours(aMat, v):
    """
    Given an adjacecy matrix aMat and a vertex v
    it returns a list of all the neighbours of v
    """
    rows, cols = len(aMat), len(aMat[0])
    nbrs = []
    for j in range(cols):
        if aMat[v][j] == 1 :
            nbrs.append(j)
    return nbrs

def findConnectionLevel(n, aMat, pX, pY):
    """
    given an adj mat aMat and two person pX and pY
    it returns min level of connectivity between person pX and pY
    """
    level, parent = {}, {}
    rows, cols = len(aMat), len(aMat[0])

    for i in range(rows):
        level[i] = -1
        parent[i] = -1

    q = []

    q.append(pX)
    level[pX] = 0

    while (len(q)>0):
        c = q.pop(0)
        for ngbr_of_c in neighbours(aMat, c):
            if level[ngbr_of_c] == -1:
                level[ngbr_of_c] = level[c] + 1
                parent[ngbr_of_c] = c
                q.append(ngbr_of_c)
            if ngbr_of_c == pY:
                break
    
    if level[pY] == -1 :
        return 0
    return level[pY]

vertices = int(input())
Amat = []
for i in range(vertices):
  row = [int(item) for item in input().split(" ")]
  Amat.append(row)
personX = int(input())
personY = int(input())
print(findConnectionLevel(vertices, Amat, personX, personY))