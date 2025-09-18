# MBPP/74
### Completion
def is_samepatterns(patterns, values):
    if len(patterns) != len(values):
        return False
    
    pattern_to_value = {}
    value_to_pattern = {}
    
    for p, v in zip(patterns, values):
        if p in pattern_to_value:
            if pattern_to_value[p] != v:
                return False
        else:
            pattern_to_value[p] = v
        
        if v in value_to_pattern:
            if value_to_pattern[v] != p:
                return False
        else:
            value_to_pattern[v] = p
            
    return True

# Test the function with the provided assertion
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
