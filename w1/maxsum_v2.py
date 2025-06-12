# Nyunt Tin
# 6632004
# Sec541

import time

inp = input()
lst = list(map(int, inp.split()))

start = time.process_time() #start time

length = len(lst)
maxSum = float("-inf") # handles negatives
for i in range(length):
    currentSum = 0
    for j in range(i, length):
        currentSum += lst[j]

        if currentSum > maxSum:
            maxSum = currentSum

finish = time.process_time() #end time
print(maxSum)
print("running time = ", finish-start)