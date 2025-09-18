# MBPP/34
### Completion
def find_missing(arr, n):
    """
    Function to find the missing number in a sorted array of integers.
    
    Parameters:
    arr (list): A sorted list of integers with one missing number.
    n (int): The number that should be present in the array.
    
    Returns:
    int: The missing number.
    """
    # Calculate the expected sum of the first n natural numbers
    expected_sum = n * (n + 1) // 2
    
    # Calculate the actual sum of the numbers present in the array
    actual_sum = sum(arr)
    
    # The missing number is the difference between expected and actual sum
    missing_number = expected_sum - actual_sum
    
    return missing_number

# Test case
assert find_missing([1, 2, 3, 5], 4) == 4
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_missing([1,2,3,5],4) == 4
    assert find_missing([1,3,4,5],4) == 2
    assert find_missing([1,2,3,5,6,7],5) == 4
