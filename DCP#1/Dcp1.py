#Daily Coding Problem #1
#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

from bisect import bisect_left

def TwoNumsAddToK(arr, k):
    arr.sort() #Sorts array in order to use binary search
    

    for i in range(len(arr)):
        target = k - arr[i]
        solution = binary_search(arr, target)

        if solution == -1:
            continue
        elif solution != i:
            return True
        elif solution + 1 < len(arr) and arr[solution + 1] == target:
            return True
        elif solution - 1 >= 0 and arr[solution - 1] == target:
            return True
    
    return False




def binary_search(arr, target):
    low = 0
    hi = len(arr)
    ind = bisect_left(arr, target, low, hi) #Provides index of target in arr

    if 0 <= ind < hi and arr[ind] == target: #Check if the found index matches our target
        return ind
    return -1
