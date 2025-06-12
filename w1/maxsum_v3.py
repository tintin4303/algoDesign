# Nyunt Tin
# 6632004
# Sec541

import time

inp = input()
lst = list(map(int, inp.split()))

def Sum_Kadane(arr):
    length = len(arr)
    if length == 0: # handles base case
        return 0
    
    max_so_far = arr[0]
    current_max = arr[0]

    for i in range(1, length):
        current_max = max(arr[i], current_max + arr[i])

        max_so_far = max(max_so_far, current_max)
    
    return max_so_far

start = time.process_time() #start time

maxSum = Sum_Kadane(lst)

finish = time.process_time() #end time
print(maxSum)
print("running time = ", finish-start)