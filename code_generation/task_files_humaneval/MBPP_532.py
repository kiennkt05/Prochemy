# MBPP/532
### Completion
from collections import Counter

def check_permutation(str1, str2):
    """
    Check if two strings are permutations of each other.

    Args:
    str1 (str): The first string.
    str2 (str): The second string.

    Returns:
    bool: True if str1 and str2 are permutations of each other, False otherwise.
    """
    # If lengths are different, they cannot be permutations
    if len(str1) != len(str2):
        return False
    
    # Count the frequency of each character in both strings
    count1 = Counter(str1)
    count2 = Counter(str2)
    
    # Compare the two frequency counts
    return count1 == count2

# Test case
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
