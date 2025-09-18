# MBPP/181
### Completion
def common_prefix(strings, n):
    if not strings:
        return ""
    
    # Take the first string as a reference
    prefix = strings[0][:n]
    
    for string in strings[1:]:
        # Compare the prefix with each string
        while string[:n] != prefix:
            # Reduce the prefix until it matches
            prefix = prefix[:-1]
            if not prefix:
                return ""
    
    return prefix

# Test the function with the provided assertion
assert common_prefix(["tablets", "tables", "taxi", "tamarind"], 4) == 'ta'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert common_prefix(["tablets", "tables", "taxi", "tamarind"], 4) == 'ta'
    assert common_prefix(["apples", "ape", "april"], 3) == 'ap'
    assert common_prefix(["teens", "teenager", "teenmar"], 3) == 'teen'
