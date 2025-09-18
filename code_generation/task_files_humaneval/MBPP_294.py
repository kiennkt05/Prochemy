# MBPP/294
### Completion
def max_val(heterogeneous_list):
    """
    Find the maximum numeric value in a heterogeneous list.

    Parameters:
    heterogeneous_list (list): A list containing elements of various types.

    Returns:
    int or float or None: The maximum numeric value if found, otherwise None.
    """
    # Filter the list to include only numeric types (int and float)
    numeric_values = [item for item in heterogeneous_list if isinstance(item, (int, float))]
    
    # Check if there are any numeric values
    if not numeric_values:
        return None  # or raise an exception if preferred
    
    # Return the maximum value from the filtered list
    return max(numeric_values)

# Test case
assert max_val(['Python', 3, 2, 4, 5, 'version']) == 5
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert max_val(['Python', 3, 2, 4, 5, 'version'])==5
    assert max_val(['Python', 15, 20, 25])==25
    assert max_val(['Python', 30, 20, 40, 50, 'version'])==50
