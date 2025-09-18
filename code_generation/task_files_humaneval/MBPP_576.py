# MBPP/576
### Completion
def is_Sub_Array(arr1, arr2, len1, len2):
    """
    Check if arr2 is a subarray of arr1.

    Parameters:
    arr1 (list): The main array to check against.
    arr2 (list): The array to check if it is a subarray of arr1.
    len1 (int): Length of arr1.
    len2 (int): Length of arr2.

    Returns:
    bool: True if arr2 is a subarray of arr1, False otherwise.
    """
    # If arr2 is longer than arr1, it cannot be a subarray
    if len2 > len1:
        return False
    
    # Iterate through arr1 to find a match for arr2
    for i in range(len1 - len2 + 1):
        # Check if the subarray matches
        if arr1[i:i + len2] == arr2:
            return True
            
    return False

# Test case
assert is_Sub_Array([1, 4, 3, 5], [1, 2], 4, 2) == False
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert is_Sub_Array([1,4,3,5],[1,2],4,2) == False
    assert is_Sub_Array([1,2,1],[1,2,1],3,3) == True
    assert is_Sub_Array([1,0,2,2],[2,2,0],4,3) ==False
