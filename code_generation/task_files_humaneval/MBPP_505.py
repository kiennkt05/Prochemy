# MBPP/505
### Completion
def re_order(arr):
    """
    Move all zeroes in the array to the end while maintaining the order of non-zero elements.

    Parameters:
    arr (list): The input list of integers.

    Returns:
    list: A new list with all zeroes moved to the end.
    """
    # List to hold non-zero elements
    non_zero_elements = []
    
    # Count of zeroes
    zero_count = 0
    
    # Iterate through the original array
    for num in arr:
        if num != 0:
            non_zero_elements.append(num)  # Add non-zero elements to the new list
        else:
            zero_count += 1  # Count the zeroes
    
    # Extend the list with the counted zeroes
    non_zero_elements.extend([0] * zero_count)
    
    return non_zero_elements

# Test case
assert re_order([6, 0, 8, 2, 3, 0, 4, 0, 1]) == [6, 8, 2, 3, 4, 1, 0, 0, 0]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert re_order([6, 0, 8, 2, 3, 0, 4, 0, 1]) == [6, 8, 2, 3, 4, 1, 0, 0, 0]
    assert re_order([4, 0, 2, 7, 0, 9, 0, 12, 0]) == [4, 2, 7, 9, 12, 0, 0, 0, 0]
    assert re_order([3, 11, 0, 74, 14, 0, 1, 0, 2]) == [3, 11, 74, 14, 1, 2, 0, 0, 0]
