# MBPP/400
### Completion
def extract_freq(tuples_list):
    # Create a set to store unique tuples
    unique_tuples = set()
    
    # Iterate through the list of tuples
    for tup in tuples_list:
        # Normalize the tuple by sorting its elements
        normalized_tup = tuple(sorted(tup))
        # Add the normalized tuple to the set
        unique_tuples.add(normalized_tup)
    
    # Return the number of unique tuples
    return len(unique_tuples)

# Test the function with the provided assertion
assert extract_freq([(3, 4), (1, 2), (4, 3), (5, 6)]) == 3
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert extract_freq([(3, 4), (1, 2), (4, 3), (5, 6)] ) == 3
    assert extract_freq([(4, 15), (2, 3), (5, 4), (6, 7)] ) == 4
    assert extract_freq([(5, 16), (2, 3), (6, 5), (6, 9)] ) == 4
