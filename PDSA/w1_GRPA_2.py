import math

def prime(n):
    prime = True
    if n > 1 :
        for i in range(2, int(math.sqrt(n) + 1)):
            if n%i == 0:
                prime = False
                break
    return prime

def prime_list(n):
    prime_list = []
    for i in range(2,n+1):
        if prime(i):
            prime_list.append(i)
    return prime_list

def Goldbach(n):
    ans = []
    pl = prime_list(int(n/2))
    # print(pl)
    for pn in pl :
        if prime(n-pn):
            ans.append((pn, n-pn))
    return ans

n=int(input())
print(sorted(Goldbach(n)))