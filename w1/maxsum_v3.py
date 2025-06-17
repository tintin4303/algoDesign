# Nyunt Tin
# 6632004
# Sec541

import time

inp = input()
lst = list(map(int, inp.split()))

def Sum_Kadane(lst):
    length = len(lst)
    if length == 0: # handles base case
        return 0
    
    max_so_far = lst[0] # max sum found so far, assign the first element 
    current_max = lst[0] # max sum at current position, assign the first element

    for i in range(1, length): # start from 1 because [0] already assigned
        current_max = max(lst[i], current_max + lst[i]) # take max from ith element from lst, and  current_max + ith element

        max_so_far = max(max_so_far, current_max) # max from max_so_far vs current_max
    
    return max_so_far

start = time.process_time() #start time
maxSum = Sum_Kadane(lst)
finish = time.process_time() #end time
print(maxSum)
print("running time = ", finish-start)

'''
Time: O(n) because it passes through the array only once

'''