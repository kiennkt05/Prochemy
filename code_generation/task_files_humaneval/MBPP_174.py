# MBPP/174
### Completion
def group_keyvalue(pairs):
    """
    Groups a sequence of key-value pairs into a dictionary of lists.

    Args:
    pairs (list of tuples): A list of tuples where each tuple contains a key and a value.

    Returns:
    dict: A dictionary where each key maps to a list of values.
    """
    result = {}
    
    for key, value in pairs:
        if key in result:
            result[key].append(value)  # Append value to existing list
        else:
            result[key] = [value]  # Create a new list for the key
    
    return result

# Test case
assert group_keyvalue([('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]) == {'yellow': [1, 3], 'blue': [2, 4], 'red': [1]}
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert group_keyvalue([('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)])=={'yellow': [1, 3], 'blue': [2, 4], 'red': [1]}
    assert group_keyvalue([('python', 1), ('python', 2), ('python', 3), ('python', 4), ('python', 5)])=={'python': [1,2,3,4,5]}
    assert group_keyvalue([('yellow',100), ('blue', 200), ('yellow', 300), ('blue', 400), ('red', 100)])=={'yellow': [100, 300], 'blue': [200, 400], 'red': [100]}
