# MBPP/490
### Completion
def extract_symmetric(tuples_list):
    # Create a set to store the tuples for quick lookup
    tuples_set = set(tuples_list)
    # Create a set to store the symmetric pairs
    symmetric_pairs = set()
    
    # Iterate through each tuple in the list
    for a, b in tuples_list:
        # Check if the symmetric pair (b, a) exists in the set
        if (b, a) in tuples_set:
            # Add the pair (a, b) to the symmetric pairs set
            symmetric_pairs.add((a, b))
    
    return symmetric_pairs

# Test the function with the provided test case
assert extract_symmetric([(6, 7), (2, 3), (7, 6), (9, 8), (10, 2), (8, 9)]) == {(8, 9), (6, 7)}
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert extract_symmetric([(6, 7), (2, 3), (7, 6), (9, 8), (10, 2), (8, 9)] ) == {(8, 9), (6, 7)}
    assert extract_symmetric([(7, 8), (3, 4), (8, 7), (10, 9), (11, 3), (9, 10)] ) == {(9, 10), (7, 8)}
    assert extract_symmetric([(8, 9), (4, 5), (9, 8), (11, 10), (12, 4), (10, 11)] ) == {(8, 9), (10, 11)}
