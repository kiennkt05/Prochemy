# MBPP/656
### Completion
def find_Min_Sum(arr1, arr2, n):
    """
    Function to find the minimum sum of absolute differences of two arrays.
    
    Parameters:
    arr1 (list): First array of integers.
    arr2 (list): Second array of integers.
    n (int): The number of elements in each array (assumed to be the same).
    
    Returns:
    int: The minimum sum of absolute differences.
    """
    # Sort both arrays
    arr1.sort()
    arr2.sort()
    
    # Calculate the sum of absolute differences
    min_sum = sum(abs(a - b) for a, b in zip(arr1, arr2))
    
    return min_sum

# Test case
assert find_Min_Sum([3, 2, 1], [2, 1, 3], 3) == 0
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_Min_Sum([3,2,1],[2,1,3],3) == 0
    assert find_Min_Sum([1,2,3],[4,5,6],3) == 9
    assert find_Min_Sum([4,1,8,7],[2,3,6,5],4) == 6
