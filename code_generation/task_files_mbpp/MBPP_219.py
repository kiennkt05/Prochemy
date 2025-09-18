# MBPP/219
### Completion
def extract_min_max(tup, k):
    # Sort the tuple to find the minimum and maximum elements
    sorted_tup = sorted(tup)
    
    # Get the minimum k elements
    min_k = sorted_tup[:k]
    
    # Get the maximum k elements
    max_k = sorted_tup[-k:]
    
    # Return the result as a tuple
    return (*min_k, *max_k)

# Test the function with the provided assertion
assert extract_min_max((5, 20, 3, 7, 6, 8), 2) == (3, 5, 8, 20)
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert extract_min_max((5, 20, 3, 7, 6, 8), 2) == (3, 5, 8, 20)
    assert extract_min_max((4, 5, 6, 1, 2, 7), 3) == (1, 2, 4, 5, 6, 7)
    assert extract_min_max((2, 3, 4, 8, 9, 11, 7), 4) == (2, 3, 4, 7, 8, 9, 11)
