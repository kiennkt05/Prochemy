# MBPP/364
### Completion
def min_flip_to_make_string_alternate(s: str) -> int:
    # Patterns for alternate characters
    pattern1 = ''.join('01'[(i % 2)] for i in range(len(s)))  # Starts with '0'
    pattern2 = ''.join('10'[(i % 2)] for i in range(len(s)))  # Starts with '1'
    
    # Count mismatches for both patterns
    count1 = sum(1 for i in range(len(s)) if s[i] != pattern1[i])
    count2 = sum(1 for i in range(len(s)) if s[i] != pattern2[i])
    
    # Return the minimum of the two counts
    return min(count1, count2)

# Test the function with the provided assertion
assert min_flip_to_make_string_alternate("0001010111") == 2
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert min_flip_to_make_string_alternate("0001010111") == 2
    assert min_flip_to_make_string_alternate("001") == 1
    assert min_flip_to_make_string_alternate("010111011") == 2 
