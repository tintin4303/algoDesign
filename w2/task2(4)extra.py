n = int(input())
k = int(input())
x = [None] * n # list of length n

def comb(i, s):
    s = sum(x)
    count = 0
    if i == n:
        for i in x:
            if i == 1:
                count += 1
        if count == k:
            print(*x)
        
    else:
        x[i] = 0
        comb(i+1)
        
        x[i] = 1
        comb(i+1)

comb(0)
