# Nyunt Tin
# 6632004
# Sec541

n = int(input())
x = [None] * n # list of length n



def comb(i):
    if i == n:
        print(*x)
    else:
        x[i] = 0
        comb(i+1)
        
        x[i] = 1
        comb(i+1)

comb(0)