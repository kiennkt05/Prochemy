# MBPP/825
### Completion
def access_elements(input_list, indices):
    """
    Access multiple elements from the input_list based on the specified indices.

    Parameters:
    input_list (list): The list from which elements will be accessed.
    indices (list): A list of indices specifying which elements to access.

    Returns:
    list: A list of elements accessed from input_list at the specified indices.
    """
    # Using list comprehension to get the elements at the specified indices
    return [input_list[i] for i in indices]

# Test case
assert access_elements([2, 3, 8, 4, 7, 9], [0, 3, 5]) == [2, 4, 9]

# If you want to test more cases, you can add additional assertions
assert access_elements([1, 2, 3, 4, 5], [1, 2]) == [2, 3]
assert access_elements(['a', 'b', 'c', 'd'], [0, 2]) == ['a', 'c']
assert access_elements([], []) == []  # Edge case: empty list and empty indices
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert access_elements([2,3,8,4,7,9],[0,3,5]) == [2, 4, 9]
    assert access_elements([1, 2, 3, 4, 5],[1,2]) == [2,3]
    assert access_elements([1,0,2,3],[0,1]) == [1,0]
