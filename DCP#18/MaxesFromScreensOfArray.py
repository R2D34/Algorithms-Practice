#Daily coding problem number 18
#Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.

#BruteForce way

def maxesFromArray_BF(array, view_len):
    maxes = []
    for view in range(len(array) - view_len + 1):
        maxes.append(max(array[ view : view + view_len ]))
    return maxes

print(maxesFromArray_BF([9,1,1,341,2,2,5,1,4,6,8,9,00,9,2], 3))
print("\n")


#Now more efficient solution

from collections import deque

def maxesFromArray(array, view_len):
    cache = deque()
    for i in range(view_len):
        while cache and array[i] >= array[cache[-1]]:
            cache.pop()
        cache.append(i)


    for i in range(view_len, len(array)):
        print(array[cache[0]])
        while cache and cache[0] <= i - view_len:
            cache.popleft()
        while cache and array[cache[-1]] <= array[i]:
            cache.pop()
        cache.append(i)
    print(array[cache[0]])


print(maxesFromArray([91,9,2,341,2,2,5,1,4,6,8,9,00,9,2], 3))
