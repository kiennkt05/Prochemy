# MBPP/709
### Completion
def get_unique(tuples):
    # Dictionary to hold the unique keys for each value
    value_to_keys = {}
    
    # Iterate through each tuple in the list
    for key, value in tuples:
        # If the value is not in the dictionary, initialize it with an empty set
        if value not in value_to_keys:
            value_to_keys[value] = set()
        # Add the key to the set of keys for this value
        value_to_keys[value].add(key)
    
    # Prepare the result dictionary with counts of unique keys
    result = {value: len(keys) for value, keys in value_to_keys.items()}
    
    # Convert the result dictionary to the required string format
    result_str = '{' + ', '.join(f'{k}: {v}' for k, v in result.items()) + '}'
    
    return result_str

# Test the function with the provided test case
assert get_unique([(3, 4), (1, 2), (2, 4), (8, 2), (7, 2), (8, 1), (9, 1), (8, 4), (10, 4)]) == '{4: 4, 2: 3, 1: 2}'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert get_unique([(3, 4), (1, 2), (2, 4), (8, 2), (7, 2), (8, 1), (9, 1), (8, 4), (10, 4)] ) == '{4: 4, 2: 3, 1: 2}'
    assert get_unique([(4, 5), (2, 3), (3, 5), (9, 3), (8, 3), (9, 2), (10, 2), (9, 5), (11, 5)] ) == '{5: 4, 3: 3, 2: 2}'
    assert get_unique([(6, 5), (3, 4), (2, 6), (11, 1), (8, 22), (8, 11), (4, 3), (14, 3), (11, 6)] ) == '{5: 1, 4: 1, 6: 2, 1: 1, 22: 1, 11: 1, 3: 2}'
