# MBPP/532
### Completion
def check_permutation(str1, str2):
    # If the lengths of the strings are not the same, they cannot be permutations
    if len(str1) != len(str2):
        return False
    
    # Sort both strings and compare
    return sorted(str1) == sorted(str2)

# Test the function with the provided assertion
assert check_permutation("abc", "cba") == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_permutation("abc", "cba") == True
    assert check_permutation("test", "ttew") == False
    assert check_permutation("xxyz", "yxzx") == True
