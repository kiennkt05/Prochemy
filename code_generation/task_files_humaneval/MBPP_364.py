# MBPP/364
### Completion
def min_flip_to_make_string_alternate(s: str) -> int:
    # Initialize counters for flips needed for both patterns
    flips_start_with_0 = 0
    flips_start_with_1 = 0
    
    # Iterate through the string and count flips for both patterns
    for i in range(len(s)):
        expected_char_for_0 = '0' if i % 2 == 0 else '1'
        expected_char_for_1 = '1' if i % 2 == 0 else '0'
        
        if s[i] != expected_char_for_0:
            flips_start_with_0 += 1
        if s[i] != expected_char_for_1:
            flips_start_with_1 += 1
            
    # Return the minimum flips required
    return min(flips_start_with_0, flips_start_with_1)

# Test case
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
