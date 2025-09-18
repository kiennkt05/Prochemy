# MBPP/158
### Completion
def min_Ops(arr, n, target):
    """
    Function to find the minimum number of operations required to make all elements in the array equal to the target value.
    
    Parameters:
    arr (list): List of integers.
    n (int): Length of the list (not strictly necessary as we can use len(arr)).
    target (int): The target value to which all elements should be made equal.
    
    Returns:
    int: Minimum number of operations required.
    """
    # Count the number of elements that are not equal to the target
    operations = sum(1 for x in arr if x != target)
    
    return operations

# Test case
assert min_Ops([2, 2, 2, 2], 4, 3) == 0  # All elements are already equal to 2, so no operations are needed.
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert min_Ops([2,2,2,2],4,3) == 0
    assert min_Ops([4,2,6,8],4,3) == -1
    assert min_Ops([21,33,9,45,63],5,6) == 24
