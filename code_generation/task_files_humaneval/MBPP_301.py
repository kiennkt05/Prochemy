# MBPP/301
### Completion
def dict_depth(d):
    # Base case: if d is not a dictionary, return 0
    if not isinstance(d, dict):
        return 0
    
    # Initialize the maximum depth
    max_depth = 0
    
    # Iterate through each value in the dictionary
    for value in d.values():
        # Recursively find the depth of the nested dictionary
        current_depth = dict_depth(value)
        # Update max_depth if current_depth is greater
        max_depth = max(max_depth, current_depth)
    
    # Return the depth of the current dictionary level + 1
    return max_depth + 1

# Test case
assert dict_depth({'a': 1, 'b': {'c': {'d': {}}}}) == 4
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}


assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4
assert dict_depth({'a':1, 'b': {'c':'python'}})==2
assert dict_depth({1: 'Sun', 2: {3: {4:'Mon'}}})==3
