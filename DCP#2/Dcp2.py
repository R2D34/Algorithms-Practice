import numpy as np

def MultiForEachInd(arr):
    new_arr = np.ones((len(arr), 1))
    np.array(arr)
    k = len(arr)
    for i in range(k):
        for j in range(k):
            if j != i:
                new_arr[j] *= arr[i]
    return new_arr

#Solution with products of numbers before the i'th index and after i'th index

def products(arr):
    #Generate prefix products
    prefix_products = []

    for num in arr:
        if prefix_products:
            prefix_products.append(prefix_products[-1] * num)
        else:
            prefix_products.append(num)

    #Generate Sufix products

    suffix_products = []
    for num in reversed(arr):
        if suffix_products:
            suffix_products.append(suffix_products[-1] * num)
        else:
            suffix_products.append(num)
    
    suffix_products = list(reversed(suffix_products))

    #Generate result

    result = []
    for i in range(len(arr)):
        if i == 0:
            result.append(suffix_products[i+1])
        elif i == len(arr) - 1:
            result.append(prefix_products[i-1])
        else:
            result.append(prefix_products[i-1] * suffix_products[i+1])
    return result

    #Works only for arrays without 0
def vectorized_products(array):
    arr_a = np.array(array)
    arr_b = np.ones(len(array))
    arr_b /= arr_a
    arr_b *= np.prod(arr_a)
    return arr_b

    #Speed comparision between implementations
    test_array = [1,2,3,4,5,6,7]
    %timeit products(test_array)
    %timeit MultiForEachInd(test_array)