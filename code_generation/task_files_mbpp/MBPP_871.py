# MBPP/871
### Completion
def are_Rotations(str1, str2):
    # Check if lengths are the same
    if len(str1) != len(str2):
        return False
    
    # Concatenate str1 with itself
    temp = str1 + str1
    
    # Check if str2 is a substring of the concatenated string
    return str2 in temp

# Test the function with the provided assertion
assert are_Rotations("abc", "cba") == False
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert are_Rotations("abc","cba") == False
    assert are_Rotations("abcd","cdba") == False
    assert are_Rotations("abacd","cdaba") == True
