# MBPP/438
### Completion
def count_bidirectional(tuples_list):
    # Create a set to store unique pairs
    seen_pairs = set()
    count = 0
    
    for a, b in tuples_list:
        # Create a bidirectional pair
        pair = (a, b)
        reverse_pair = (b, a)
        
        # Check if the reverse pair is already in the set
        if reverse_pair in seen_pairs:
            count += 1
        
        # Add the current pair to the set
        seen_pairs.add(pair)
    
    return str(count)

# Test the function with the provided assertion
assert count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 1), (6, 5), (2, 1)]) == '3'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 1), (6, 5), (2, 1)] ) == '3'
    assert count_bidirectional([(5, 6), (1, 3), (6, 5), (9, 1), (6, 5), (2, 1)] ) == '2'
    assert count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 2), (6, 5), (2, 1)] ) == '4'
