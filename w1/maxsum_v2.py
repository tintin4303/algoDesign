# Nyunt Tin
# 6632004
# Sec541

import time

inp = input()
lst = list(map(int, inp.split()))
length = len(lst)


def Sum(accumulated, i, j):
    if i == 0:
        return accumulated[j]
    return accumulated[j] - accumulated[i-1]

def find_max(lst): 
    accumulated = [] # list of sums, each element is sum of prev elements
    acc = 0 # accumulator

    for i in lst: # iterate through lst
        acc += i # sum all i to acc
        accumulated.append(acc) # append to list
        # sum from start to finish append to accumulated

    largest_sum = float("-inf") # handle negatives

    for i in range(length): # i start index
        for j in range(i, length): # j end index
            subsequence_sum = Sum(accumulated, i, j) # calc sum of subarrays from i to j

            if subsequence_sum > largest_sum: # replace largest if larger
                largest_sum = subsequence_sum
    
    return largest_sum

start = time.process_time() #start time
print(find_max(lst))
finish = time.process_time() #end time

print("running time = ", finish-start)

'''
Time: O(n^2) because of first loop O(n) and a nested loop which has 2 for loops 
but the inner loop doesn't always run n times, unlike the outer loop (altogether O(n))
'''