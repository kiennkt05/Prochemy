# MBPP/790
### Completion
def even_position(lst):
    """
    Check if every even index in the list contains an even number.

    Parameters:
    lst (list): The list of numbers to check.

    Returns:
    bool: True if all even indices contain even numbers, False otherwise.
    """
    for i in range(0, len(lst), 2):  # Iterate over even indices
        if lst[i] % 2 != 0:  # Check if the number at the even index is odd
            return False  # Return False if an odd number is found
    return True  # Return True if all even indices contain even numbers

# Test cases
assert even_position([3, 2, 1]) == False  # 3 is at index 0 (odd)
assert even_position([2, 4, 6]) == True    # 2 and 6 are at even indices (0 and 2)
assert even_position([0, 1, 4, 3]) == True  # 0 and 4 are at even indices (0 and 2)
assert even_position([1, 2, 3, 4]) == False # 1 is at index 0 (odd)
assert even_position([]) == True            # Empty list, vacuously true

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert even_position([3,2,1]) == False
    assert even_position([1,2,3]) == False
    assert even_position([2,1,4]) == True
