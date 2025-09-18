# MBPP/559
### Completion
def max_sub_array_sum(arr, n):
    """
    Function to find the largest sum of contiguous subarray in the given array.
    
    Parameters:
    arr (list): The input array of integers.
    n (int): The size of the array.
    
    Returns:
    int: The maximum sum of the contiguous subarray.
    """
    if n == 0:
        return 0  # If the array is empty, return 0
    
    max_current = arr[0]
    max_global = arr[0]
    
    for i in range(1, n):
        max_current = max(arr[i], max_current + arr[i])
        if max_current > max_global:
            max_global = max_current
            
    return max_global

# Test case
assert max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8) == 7
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8) == 7
    assert max_sub_array_sum([-3, -4, 5, -2, -3, 2, 6, -4], 8) == 8
    assert max_sub_array_sum([-4, -5, 6, -3, -4, 3, 7, -5], 8) == 10
