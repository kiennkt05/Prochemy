# MBPP/650
### Completion
def are_Equal(arr1, arr2, n1, n2):
    """
    Check if two arrays are equal.

    Parameters:
    arr1 (list): First array.
    arr2 (list): Second array.
    n1 (int): Length of the first array.
    n2 (int): Length of the second array.

    Returns:
    bool: True if both arrays are equal, False otherwise.
    """
    # If lengths are not equal, arrays cannot be equal
    if n1 != n2:
        return False
    
    # Sort both arrays
    sorted_arr1 = sorted(arr1)
    sorted_arr2 = sorted(arr2)
    
    # Compare sorted arrays
    return sorted_arr1 == sorted_arr2

# Test case
assert are_Equal([1, 2, 3], [3, 2, 1], 3, 3) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert are_Equal([1,2,3],[3,2,1],3,3) == True
    assert are_Equal([1,1,1],[2,2,2],3,3) == False
    assert are_Equal([8,9],[4,5,6],2,3) == False
