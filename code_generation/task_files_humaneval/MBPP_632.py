# MBPP/632
### Completion
def move_zero(lst):
    """
    Move all zeroes in the list to the end while maintaining the order of non-zero elements.

    Parameters:
    lst (list): The input list containing integers.

    Returns:
    list: A new list with all zeroes moved to the end.
    """
    # Create a list for non-zero elements
    non_zero_elements = [x for x in lst if x != 0]
    
    # Count the number of zeroes
    zero_count = lst.count(0)
    
    # Append the zeroes to the end of the non-zero elements
    result = non_zero_elements + [0] * zero_count
    
    return result

# Test case
assert move_zero([1, 0, 2, 0, 3, 4]) == [1, 2, 3, 4, 0, 0]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert move_zero([1,0,2,0,3,4]) == [1,2,3,4,0,0]
    assert move_zero([2,3,2,0,0,4,0,5,0]) == [2,3,2,4,5,0,0,0,0]
    assert move_zero([0,1,0,1,1]) == [1,1,1,0,0]
