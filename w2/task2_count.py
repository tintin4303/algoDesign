n = int(input())
x = [None] * n # list of length n
count = 0


def comb(i):
    global count
    if i == n:
        count += 1
    else:
        x[i] = 0
        comb(i+1)
        
        x[i] = 1
        comb(i+1)

comb(0)
print(count)