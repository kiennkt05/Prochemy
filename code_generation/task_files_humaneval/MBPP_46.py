# MBPP/46
### Completion
def test_distinct(numbers):
    """
    Determine whether all numbers in the list are distinct.

    Parameters:
    numbers (list): A list of numbers to check for distinctness.

    Returns:
    bool: True if all numbers are distinct, False otherwise.
    """
    # Convert the list to a set to remove duplicates
    unique_numbers = set(numbers)
    
    # Compare the length of the set with the original list
    return len(unique_numbers) == len(numbers)

# Test case
assert test_distinct([1, 5, 7, 9]) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert test_distinct([1,5,7,9]) == True
    assert test_distinct([2,4,5,5,7,9]) == False
    assert test_distinct([1,2,3]) == True
