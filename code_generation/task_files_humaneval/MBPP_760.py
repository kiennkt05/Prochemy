# MBPP/760
### Completion
def unique_Element(arr, n):
    """
    Check if the array contains only one distinct element.

    Parameters:
    arr (list): The input array to check.
    n (int): The length of the array.

    Returns:
    str: 'YES' if all elements are the same, 'NO' otherwise.
    """
    # Check if the array is empty
    if n == 0:
        return 'NO'  # An empty array does not have a distinct element

    # Use a set to find distinct elements
    distinct_elements = set(arr)

    # If the length of the set is 1, all elements are the same
    if len(distinct_elements) == 1:
        return 'YES'
    else:
        return 'NO'

# Test case
assert unique_Element([1, 1, 1], 3) == 'YES'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert unique_Element([1,1,1],3) == 'YES'
    assert unique_Element([1,2,1,2],4) == 'NO'
    assert unique_Element([1,2,3,4,5],5) == 'NO'
