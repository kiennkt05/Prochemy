# MBPP/871
### Completion
def are_Rotations(str1, str2):
    """
    Check if str1 and str2 are rotations of each other.

    Parameters:
    str1 (str): The first string.
    str2 (str): The second string.

    Returns:
    bool: True if str1 and str2 are rotations of each other, False otherwise.
    """
    # Check if the lengths of the strings are the same
    if len(str1) != len(str2):
        return False
    
    # Concatenate str1 with itself
    concatenated = str1 + str1
    
    # Check if str2 is a substring of the concatenated string
    return str2 in concatenated

# Test cases
assert are_Rotations("abc", "cba") == False  # Example provided
assert are_Rotations("abc", "bca") == True    # "bca" is a rotation of "abc"
assert are_Rotations("abc", "cab") == True    # "cab" is a rotation of "abc"
assert are_Rotations("abc", "abc") == True    # Same strings are rotations
assert are_Rotations("abcd", "dabc") == True   # "dabc" is a rotation of "abcd"
assert are_Rotations("abcd", "abcd") == True   # Same strings are rotations
assert are_Rotations("abcd", "abdc") == False  # "abdc" is not a rotation of "abcd"

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert are_Rotations("abc","cba") == False
    assert are_Rotations("abcd","cdba") == False
    assert are_Rotations("abacd","cdaba") == True
