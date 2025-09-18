# MBPP/400
### Completion
def extract_freq(tuples_list):
    """
    Extract the frequency of unique tuples in the given list, treating tuples as identical
    regardless of the order of their elements.

    Parameters:
    tuples_list (list of tuples): A list of tuples to analyze.

    Returns:
    int: The count of unique tuples.
    """
    # Use a set to store unique normalized tuples
    unique_tuples = set()
    
    for tup in tuples_list:
        # Normalize the tuple by sorting its elements
        normalized_tup = tuple(sorted(tup))
        unique_tuples.add(normalized_tup)
    
    # The number of unique tuples is the size of the set
    return len(unique_tuples)

# Test case
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
