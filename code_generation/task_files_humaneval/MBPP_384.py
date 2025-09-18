# MBPP/384
### Completion
def frequency_of_smallest(n, arr):
    """
    This function finds the frequency of the smallest value in the given array.
    
    Parameters:
    n (int): The number of elements in the array (not used in the function but included for signature).
    arr (list): The list of integers to search through.
    
    Returns:
    int: The frequency of the smallest value in the array.
    """
    if not arr:  # Check if the array is empty
        return 0
    
    # Find the smallest value in the array
    smallest_value = min(arr)
    
    # Count the occurrences of the smallest value
    frequency = arr.count(smallest_value)
    
    return frequency

# Test case
assert frequency_of_smallest(5, [1, 2, 3, 4, 3]) == 1
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert frequency_Of_Smallest(5,[1,2,3,4,3]) == 1
    assert frequency_Of_Smallest(7,[3,1,2,5,6,2,3]) == 1
    assert frequency_Of_Smallest(7,[3,3,6,3,7,4,9]) == 3
