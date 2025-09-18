# MBPP/19
### Completion
def test_duplicate(arr):
    """
    Function to check if there are any duplicate elements in the given array.
    
    Parameters:
    arr (list): A list of integers to check for duplicates.
    
    Returns:
    bool: True if there are duplicates, False otherwise.
    """
    seen = set()  # Initialize an empty set to keep track of seen elements
    for num in arr:
        if num in seen:
            return True  # Duplicate found
        seen.add(num)  # Add the number to the set
    return False  # No duplicates found

# Test case
assert test_duplicate([1, 2, 3, 4, 5]) == False  # No duplicates
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert test_duplicate(([1,2,3,4,5]))==False
    assert test_duplicate(([1,2,3,4, 4]))==True
    assert test_duplicate([1,1,2,2,3,3,4,4,5])==True
