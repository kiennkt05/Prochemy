# MBPP/414
### Completion
def overlapping(seq1, seq2):
    """
    Check if there are any common elements between two sequences.

    Parameters:
    seq1 (iterable): The first sequence to check.
    seq2 (iterable): The second sequence to check.

    Returns:
    bool: True if there is at least one common element, False otherwise.
    """
    # Convert the second sequence to a set for faster lookup
    set_seq2 = set(seq2)
    
    # Check for any common elements
    for item in seq1:
        if item in set_seq2:
            return True
            
    return False

# Test case
assert overlapping([1, 2, 3, 4, 5], [6, 7, 8, 9]) == False
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert overlapping([1,2,3,4,5],[6,7,8,9]) == False
    assert overlapping([1,2,3],[4,5,6]) == False
    assert overlapping([1,4,5],[1,4,5]) == True
