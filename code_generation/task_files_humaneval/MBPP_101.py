# MBPP/101
### Completion
def kth_element(arr, n, k):
    """
    Find the k-th smallest element in the given array.

    Parameters:
    arr (list): The input array of integers.
    n (int): The size of the array.
    k (int): The position of the element to find (1-based index).

    Returns:
    int: The k-th smallest element in the array.
    """
    # Sort the array
    sorted_arr = sorted(arr)
    
    # Return the k-th smallest element (1-based index)
    return sorted_arr[k - 1]

# Test case
assert kth_element([12, 3, 5, 7, 19], 5, 2) == 3
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert kth_element([12,3,5,7,19], 5, 2) == 3
    assert kth_element([17,24,8,23], 4, 3) == 8
    assert kth_element([16,21,25,36,4], 5, 4) == 36
