# MBPP/464
### Completion
def check_value(input_dict, value):
    """
    Check if all values in the input dictionary are the same and equal to the specified value.

    Parameters:
    input_dict (dict): The dictionary to check.
    value: The value to compare against.

    Returns:
    bool: True if all values are the same and equal to the specified value, False otherwise.
    """
    # Get the unique values from the dictionary
    unique_values = set(input_dict.values())
    
    # Check if all values are the same and equal to the provided value
    return len(unique_values) == 1 and value in unique_values

# Test case
assert check_value({'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}, 10) == False
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_value({'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12},10)==False
    assert check_value({'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12},12)==True
    assert check_value({'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12},5)==False
