# MBPP/237
### Completion
def check_occurences(tuples_list):
    # Dictionary to hold the counts of occurrences
    occurrences = {}
    
    for tup in tuples_list:
        # Create a sorted version of the tuple to handle (a, b) and (b, a) as the same
        sorted_tup = tuple(sorted(tup))
        
        # Increment the count for the sorted tuple
        if sorted_tup in occurrences:
            occurrences[sorted_tup] += 1
        else:
            occurrences[sorted_tup] = 1
    
    # Prepare the final result dictionary with the original tuples
    result = {}
    for tup, count in occurrences.items():
        # Only include the original tuples in the result
        if count > 1:  # Only include tuples that occur more than once
            result[tup] = count
    
    return result

# Test case
assert check_occurences([(3, 1), (1, 3), (2, 5), (5, 2), (6, 3)]) == {(1, 3): 2, (2, 5): 2}
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_occurences([(3, 1), (1, 3), (2, 5), (5, 2), (6, 3)] ) == {(1, 3): 2, (2, 5): 2, (3, 6): 1}
    assert check_occurences([(4, 2), (2, 4), (3, 6), (6, 3), (7, 4)] ) == {(2, 4): 2, (3, 6): 2, (4, 7): 1}
    assert check_occurences([(13, 2), (11, 23), (12, 25), (25, 12), (16, 23)] ) == {(2, 13): 1, (11, 23): 1, (12, 25): 2, (16, 23): 1}
