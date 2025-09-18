# MBPP/410
### Completion
def min_val(heterogeneous_list):
    """
    Find the minimum numeric value in a heterogeneous list.

    Parameters:
    heterogeneous_list (list): A list containing elements of various types.

    Returns:
    int or float or None: The minimum numeric value if found, otherwise None.
    """
    # Filter the list to include only numeric types (int and float)
    numeric_values = [item for item in heterogeneous_list if isinstance(item, (int, float))]
    
    # Check if there are any numeric values
    if not numeric_values:
        return None  # or raise an exception if preferred
    
    # Return the minimum value from the filtered list
    return min(numeric_values)

# Test case
assert min_val(['Python', 3, 2, 4, 5, 'version']) == 2
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert min_val(['Python', 3, 2, 4, 5, 'version'])==2
    assert min_val(['Python', 15, 20, 25])==15
    assert min_val(['Python', 30, 20, 40, 50, 'version'])==20
