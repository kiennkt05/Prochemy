# MBPP/378
### Completion
def move_first(lst):
    """
    Shift the last element of the list to the first position.

    Parameters:
    lst (list): The list from which the last element will be moved to the front.

    Returns:
    list: A new list with the last element moved to the first position.
    """
    # Check if the list is empty
    if not lst:
        return lst  # Return the empty list as is

    # Move the last element to the front
    return [lst[-1]] + lst[:-1]

# Test case
assert move_first([1, 2, 3, 4]) == [4, 1, 2, 3]

# Additional test cases
assert move_first([]) == []  # Edge case: empty list
assert move_first([5]) == [5]  # Edge case: single element
assert move_first([1, 2]) == [2, 1]  # Two elements
assert move_first([10, 20, 30, 40, 50]) == [50, 10, 20, 30, 40]  # Multiple elements

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert move_first([1,2,3,4]) == [4,1,2,3]
    assert move_first([0,1,2,3]) == [3,0,1,2]
    assert move_first([9,8,7,1]) == [1,9,8,7]
