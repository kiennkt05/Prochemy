# MBPP/885
### Completion
def is_Isomorphic(s1: str, s2: str) -> bool:
    # If the lengths of the strings are not the same, they cannot be isomorphic
    if len(s1) != len(s2):
        return False
    
    # Create two dictionaries to store the mappings
    mapping_s1_to_s2 = {}
    mapping_s2_to_s1 = {}
    
    for char1, char2 in zip(s1, s2):
        # Check the mapping from s1 to s2
        if char1 in mapping_s1_to_s2:
            if mapping_s1_to_s2[char1] != char2:
                return False
        else:
            mapping_s1_to_s2[char1] = char2
        
        # Check the mapping from s2 to s1
        if char2 in mapping_s2_to_s1:
            if mapping_s2_to_s1[char2] != char1:
                return False
        else:
            mapping_s2_to_s1[char2] = char1
    
    return True

# Test case
assert is_Isomorphic("paper", "title") == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert is_Isomorphic("paper","title") == True
    assert is_Isomorphic("ab","ba") == True
    assert is_Isomorphic("ab","aa") == False
