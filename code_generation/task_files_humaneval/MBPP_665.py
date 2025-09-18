# MBPP/665
### Completion
def move_last(lst):
    """
    Shifts the first element of the list to the end of the list.

    Parameters:
    lst (list): The list from which the first element will be moved to the end.

    Returns:
    list: The modified list with the first element moved to the end.
    """
    # Check if the list is empty or has only one element
    if len(lst) <= 1:
        return lst
    
    # Remove the first element
    first_element = lst.pop(0)
    
    # Append the first element to the end of the list
    lst.append(first_element)
    
    return lst

# Test case
assert move_last([1, 2, 3, 4]) == [2, 3, 4, 1]

# Additional test cases for verification
assert move_last([]) == []  # Empty list should return empty list
assert move_last([5]) == [5]  # Single element list should return the same list
assert move_last([10, 20, 30]) == [20, 30, 10]  # General case
assert move_last([1, 2]) == [2, 1]  # Two elements case

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert move_last([1,2,3,4]) == [2,3,4,1]
    assert move_last([2,3,4,1,5,0]) == [3,4,1,5,0,2]
    assert move_last([5,4,3,2,1]) == [4,3,2,1,5]
