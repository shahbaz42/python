# https://codeforces.com/contest/1513/problem/C

def gen_seq(q, n):
    seq = [q]
    for i in range(9):
        new = []
        for j in seq[-1]:
            new.append(str(int(j)+1))
        seq.append("".join(str(x) for x in new))
 
    seq_len = [len(x) for x in seq]
    # print(seq)
    # print(seq_len)
 
    if n > 10:
        for i in range(n-10):
            seq_len.append(seq_len[i+1]+seq_len[i])
        return seq_len
    else:
        return seq_len[:n+1]
 
 
 
# def sol(q, n):
#     seq = generate_sequence(q+n)
#     return seq
 
# print(generate_sequence(20)
# ans = gen_seq("12", 101)[-1]
# print(ans % (10**9+7))
 
n = int(input())
 
for i in range(n):
    q, n = input().split()
    n = int(n)
    ans = gen_seq(q, n+1)[-1]
    print(ans % (10**9+7))