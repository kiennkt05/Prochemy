# MBPP/908
### Completion
def find_fixed_point(arr, n):
    """
    Function to find the fixed point in the given array.
    
    A fixed point is an index i such that arr[i] == i.
    
    Parameters:
    arr (list): The input array of integers.
    n (int): The size of the array.
    
    Returns:
    int: The fixed point index if found, otherwise -1.
    """
    for i in range(n):
        if arr[i] == i:
            return i  # Return the fixed point index
    return -1  # Return -1 if no fixed point is found

# Test case
assert find_fixed_point([-10, -1, 0, 3, 10, 11, 30, 50, 100], 9) == 3
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_fixed_point([-10, -1, 0, 3, 10, 11, 30, 50, 100],9) == 3
    assert find_fixed_point([1, 2, 3, 4, 5, 6, 7, 8],8) == -1
    assert find_fixed_point([0, 2, 5, 8, 17],5) == 0
