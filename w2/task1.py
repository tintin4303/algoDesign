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



'''
 input: 3, output =
    000
    001
    010
    011
    100
    101
    110
    111
'''
comb(0)