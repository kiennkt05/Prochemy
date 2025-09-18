# MBPP/22
### Completion
def find_first_duplicate(arr):
    """
    Function to find the first duplicate element in an array of integers.
    
    Parameters:
    arr (list): A list of integers.
    
    Returns:
    int or None: The first duplicate integer if found, otherwise None.
    """
    seen = set()  # Set to keep track of seen elements
    
    for num in arr:
        if num in seen:
            return num  # Return the first duplicate found
        seen.add(num)  # Add the number to the set if not seen
    
    return None  # Return None if no duplicates are found

# Test case
assert find_first_duplicate([1, 2, 3, 4, 4, 5]) == 4
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_first_duplicate(([1, 2, 3, 4, 4, 5]))==4
    assert find_first_duplicate([1, 2, 3, 4])==-1
    assert find_first_duplicate([1, 1, 2, 3, 3, 2, 2])==1
