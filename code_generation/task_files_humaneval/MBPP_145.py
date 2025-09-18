# MBPP/145
### Completion
def max_Abs_Diff(arr, n):
    """
    Function to find the maximum difference between any two elements in the given array.
    
    Parameters:
    arr (tuple): A tuple of integers.
    n (int): The number of elements in the array.
    
    Returns:
    int: The maximum absolute difference between any two elements.
    """
    # Convert tuple to a list for easier manipulation
    arr_list = list(arr)
    
    # Find the maximum and minimum values in the array
    max_value = max(arr_list)
    min_value = min(arr_list)
    
    # Calculate the maximum difference
    max_difference = max_value - min_value
    
    return max_difference

# Test case
assert max_Abs_Diff((2, 1, 5, 3), 4) == 4
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert max_Abs_Diff((2,1,5,3),4) == 4
    assert max_Abs_Diff((9,3,2,5,1),5) == 8
    assert max_Abs_Diff((3,2,1),3) == 2
