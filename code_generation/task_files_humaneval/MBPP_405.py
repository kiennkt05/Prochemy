# MBPP/405
### Completion
def check_tuplex(tup, element):
    """
    Check if an element exists within a tuple.

    Parameters:
    tup (tuple): The tuple to search within.
    element: The element to search for.

    Returns:
    bool: True if the element exists in the tuple, False otherwise.
    """
    return element in tup

# Test case
assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), 'r') == True

# Additional test cases for verification
assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), 'x') == False
assert check_tuplex((), 'r') == False
assert check_tuplex(("a", "b", "c"), 'b') == True
assert check_tuplex(("1", "2", "3"), 2) == False  # Different type check

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'r')==True
    assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),'5')==False
    assert check_tuplex(("w", 3, "r", "e", "s", "o", "u", "r", "c","e"),3)==True
