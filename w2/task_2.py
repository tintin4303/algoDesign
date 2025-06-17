# Nyunt Tin
# 6632004
# Sec541

n = int(input())
k = int(input())
x = [None] * n # list of length n

def count_ones(x):
    count = 0
    for i in x:
            if i == 1:
                count += 1
    return count

def comb(i):
    if i == n:
        count = count_ones(x)
        if count == k:
            print(*x)
        
    else:
        x[i] = 0
        comb(i+1)
        
        x[i] = 1
        comb(i+1)

comb(0)
