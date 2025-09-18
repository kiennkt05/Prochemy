# MBPP/438
### Completion
def count_bidirectional(tuples_list):
    # Set to keep track of seen tuples
    seen = set()
    # Set to keep track of counted bidirectional pairs
    counted_pairs = set()
    
    for a, b in tuples_list:
        # Create a bidirectional pair representation
        pair = (min(a, b), max(a, b))
        
        # Check if the reverse pair has been seen
        if pair in counted_pairs:
            continue
        
        # Check if the reverse of the current tuple exists in seen
        if (b, a) in seen:
            counted_pairs.add(pair)
        
        # Add the current tuple to the seen set
        seen.add((a, b))
    
    # Return the count of unique bidirectional pairs as a string
    return str(len(counted_pairs))

# Test case
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
