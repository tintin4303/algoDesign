# Nyunt Tin
# 6632004
# Sec541

import time

inp = input()
lst = list(map(int, inp.split()))
n = len(lst)

def Sum(x, i, j): # sum range 0->1, 0->2 etc depending on outer loop
    s = 0
    for k in range(i, j+1):
        s += x[k]
    return s

start = time.process_time() #start time

maxSum = float("-inf") # handle negative inf
length = len(lst)
for i in range(length): 
    for j in range(i, length):
        currentSum = Sum(lst, i, j)
        if currentSum > maxSum: # compare and reassign 
            maxSum = currentSum 
finish = time.process_time() # end time
print(maxSum)
print("running time = ", finish-start)

''' 
this brute force method works with 3 loops -> O(n^3) time
innermost loop in Sum(): sum up all values from i to j+1, when i=0 & j=0, result = sum of range 0->0+1 which is first index, then i=0,j=1, repeat till middle loop is finished
middleloop and outerloop change input value inside innermost loop: i=0 & j=0, i=0 & j=1, ... till middle loop ends, then start again from i=1 & j=0, ... till outermost loop ends
'''