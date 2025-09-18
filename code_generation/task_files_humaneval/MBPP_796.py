# MBPP/796
### Completion
def return_sum(input_dict):
    """
    Calculate the sum of all values in the given dictionary.

    Parameters:
    input_dict (dict): A dictionary with numeric values.

    Returns:
    int: The sum of all values in the dictionary.
    """
    # Use the sum function on the values of the dictionary
    total_sum = sum(input_dict.values())
    return total_sum

# Test case
assert return_sum({'a': 100, 'b': 200, 'c': 300}) == 600
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert return_sum({'a': 100, 'b':200, 'c':300}) == 600
    assert return_sum({'a': 25, 'b':18, 'c':45}) == 88
    assert return_sum({'a': 36, 'b':39, 'c':49}) == 124
