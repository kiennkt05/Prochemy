# MBPP/281
### Completion
def all_unique(lst):
    """
    Check if all elements in the given list are unique.

    Parameters:
    lst (list): The list to check for uniqueness.

    Returns:
    bool: True if all elements are unique, False otherwise.
    """
    # Convert the list to a set to remove duplicates
    unique_elements = set(lst)
    
    # Compare the length of the set with the original list
    return len(unique_elements) == len(lst)

# Test cases
assert all_unique([1, 2, 3]) == True  # All elements are unique
assert all_unique([1, 2, 2, 3]) == False  # The element '2' is duplicated
assert all_unique([]) == True  # An empty list is considered to have unique elements
assert all_unique([1]) == True  # A single element is unique
assert all_unique([1, 1, 1, 1]) == False  # All elements are the same

print("All tests passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert all_unique([1,2,3]) == True
    assert all_unique([1,2,1,2]) == False
    assert all_unique([1,2,3,4,5]) == True
