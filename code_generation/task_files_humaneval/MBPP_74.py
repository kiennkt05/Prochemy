# MBPP/74
### Completion
def is_samepatterns(patterns, values):
    # Create two dictionaries to hold the mappings
    pattern_to_value = {}
    value_to_pattern = {}
    
    # Iterate through both lists simultaneously
    for p, v in zip(patterns, values):
        # Check the mapping from pattern to value
        if p in pattern_to_value:
            if pattern_to_value[p] != v:
                return False  # Inconsistent mapping
        else:
            pattern_to_value[p] = v
        
        # Check the mapping from value to pattern
        if v in value_to_pattern:
            if value_to_pattern[v] != p:
                return False  # Inconsistent mapping
        else:
            value_to_pattern[v] = p
    
    return True  # All mappings are consistent

# Test case
assert is_samepatterns(["red", "green", "green"], ["a", "b", "b"]) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert is_samepatterns(["red","green","green"], ["a", "b", "b"])==True 
    assert is_samepatterns(["red","green","greenn"], ["a","b","b"])==False 
    assert is_samepatterns(["red","green","greenn"], ["a","b"])==False 
