# MBPP/465
### Completion
def drop_empty(input_dict):
    """
    Drops items with None values from the given dictionary.

    Parameters:
    input_dict (dict): The dictionary from which to drop empty items.

    Returns:
    dict: A new dictionary with empty items removed.
    """
    # Using dictionary comprehension to filter out None values
    return {key: value for key, value in input_dict.items() if value is not None}

# Test case
assert drop_empty({'c1': 'Red', 'c2': 'Green', 'c3': None}) == {'c1': 'Red', 'c2': 'Green'}

# Additional test cases for verification
assert drop_empty({'a': 1, 'b': None, 'c': 3}) == {'a': 1, 'c': 3}
assert drop_empty({'x': None, 'y': None}) == {}
assert drop_empty({'key1': 'value1', 'key2': '', 'key3': 0}) == {'key1': 'value1', 'key2': '', 'key3': 0}
assert drop_empty({}) == {}
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert drop_empty({'c1': 'Red', 'c2': 'Green', 'c3':None})=={'c1': 'Red', 'c2': 'Green'}
    assert drop_empty({'c1': 'Red', 'c2': None, 'c3':None})=={'c1': 'Red'}
    assert drop_empty({'c1': None, 'c2': 'Green', 'c3':None})=={ 'c2': 'Green'}
