# Kadane's algorithm is a popular algorithm to find the subarray with the largest sum in a given array of integers. 
# The algorithm runs in  O(n) time complexity and is based on dynamic programming principles.


def max_subarray_sum(arr):
    max_so_far = float('-inf')
    max_ending_here = 0
    
    for num in arr:
        max_ending_here += num
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
        if max_ending_here < 0:
            max_ending_here = 0
    
    return max_so_far