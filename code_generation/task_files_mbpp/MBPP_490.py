# MBPP/490
### Completion
def extract_symmetric(tuple_list):
    symmetric_pairs = set()
    seen = set()

    for pair in tuple_list:
        # Add the pair to the seen set
        seen.add(pair)
        # Check for the symmetric pair
        symmetric_pair = (pair[1], pair[0])
        if symmetric_pair in seen:
            symmetric_pairs.add(pair)
            symmetric_pairs.add(symmetric_pair)

    return symmetric_pairs

# Test the function with the provided assertion
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
