# MBPP/414
### Completion
def overlapping(seq1, seq2):
    # Check if there is any common element in both sequences
    return any(item in seq2 for item in seq1)

# Test the function with the provided assertion
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
