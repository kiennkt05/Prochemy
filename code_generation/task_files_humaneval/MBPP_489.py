# MBPP/489
### Completion
def frequency_of_largest(n, arr):
    """
    Function to find the frequency of the largest value in a given array.
    
    Parameters:
    n (int): The number of elements in the array (not used in the function but included for signature).
    arr (list): The list of integers to analyze.
    
    Returns:
    int: The frequency of the largest value in the array.
    """
    if not arr:  # Check if the array is empty
        return 0
    
    largest_value = max(arr)  # Find the largest value in the array
    frequency = arr.count(largest_value)  # Count how many times the largest value appears
    
    return frequency

# Test case
assert frequency_of_largest(5, [1, 2, 3, 4, 4]) == 2
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert frequency_Of_Largest(5,[1,2,3,4,4]) == 2
    assert frequency_Of_Largest(3,[5,6,5]) == 1
    assert frequency_Of_Largest(4,[2,7,7,7]) == 3
