# MBPP/659
### Completion
def Repeat(numbers):
    """
    Function to find and return a list of duplicate integers from the input list.
    
    Parameters:
    numbers (list): A list of integers to check for duplicates.
    
    Returns:
    list: A list of duplicate integers found in the input list.
    """
    seen = set()        # Set to track seen numbers
    duplicates = set()  # Set to track duplicates

    for number in numbers:
        if number in seen:
            duplicates.add(number)  # Add to duplicates if already seen
        else:
            seen.add(number)        # Add to seen if not seen before

    return list(duplicates)  # Convert duplicates set to a list and return

# Test case
assert Repeat([10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]) == [20, 30, -20, 60]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert Repeat([10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]) == [20, 30, -20, 60]
    assert Repeat([-1, 1, -1, 8]) == [-1]
    assert Repeat([1, 2, 3, 1, 2,]) == [1, 2]
