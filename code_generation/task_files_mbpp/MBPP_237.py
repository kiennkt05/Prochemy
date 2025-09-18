# MBPP/237
### Completion
def check_occurrences(tuples_list):
    from collections import defaultdict
    
    # Create a dictionary to count occurrences
    occurrences = defaultdict(int)
    
    # Count occurrences of each tuple
    for tup in tuples_list:
        occurrences[tup] += 1
    
    # Create a result dictionary to store tuples with their counts
    result = {}
    
    # Filter the occurrences to include only those with more than 1 occurrence
    for tup, count in occurrences.items():
        if count > 1:
            result[tup] = count
    
    return result

# Test the function with the provided assertion
assert check_occurrences([(3, 1), (1, 3), (2, 5), (5, 2), (6, 3)]) == {(1, 3): 2, (2, 5): 2}
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_occurences([(3, 1), (1, 3), (2, 5), (5, 2), (6, 3)] ) == {(1, 3): 2, (2, 5): 2, (3, 6): 1}
    assert check_occurences([(4, 2), (2, 4), (3, 6), (6, 3), (7, 4)] ) == {(2, 4): 2, (3, 6): 2, (4, 7): 1}
    assert check_occurences([(13, 2), (11, 23), (12, 25), (25, 12), (16, 23)] ) == {(2, 13): 1, (11, 23): 1, (12, 25): 2, (16, 23): 1}
