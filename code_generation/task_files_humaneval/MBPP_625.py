# MBPP/625
### Completion
def swap_List(lst):
    """
    Swap the first and last elements of the given list.

    Parameters:
    lst (list): The list whose first and last elements are to be swapped.

    Returns:
    list: The list with the first and last elements swapped.
    """
    # Check if the list is empty or has only one element
    if len(lst) <= 1:
        return lst
    
    # Swap the first and last elements
    lst[0], lst[-1] = lst[-1], lst[0]
    
    return lst

# Test case
assert swap_List([1, 2, 3]) == [3, 2, 1]

# Additional test cases
assert swap_List([1]) == [1]  # Single element list
assert swap_List([]) == []     # Empty list
assert swap_List([1, 2]) == [2, 1]  # Two element list
assert swap_List([1, 2, 3, 4]) == [4, 2, 3, 1]  # More than two elements

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert swap_List([1,2,3]) == [3,2,1]
    assert swap_List([1,2,3,4,4]) == [4,2,3,4,1]
    assert swap_List([4,5,6]) == [6,5,4]
