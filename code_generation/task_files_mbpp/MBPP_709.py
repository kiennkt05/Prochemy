# MBPP/709
### Completion
def get_unique(pairs):
    value_to_keys = {}
    
    for key, value in pairs:
        if value not in value_to_keys:
            value_to_keys[value] = set()  # Use a set to store unique keys
        value_to_keys[value].add(key)
    
    # Count the unique keys for each value
    unique_counts = {value: len(keys) for value, keys in value_to_keys.items()}
    
    # Format the output as a string
    return str(unique_counts)

# Test the function with the provided assertion
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
