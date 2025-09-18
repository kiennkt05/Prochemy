# MBPP/9
### Completion
def find_rotations(s: str) -> int:
    # Get the length of the string
    n = len(s)
    
    # If the string is empty or has only one character, return 1
    if n <= 1:
        return 1
    
    # Check for the minimum rotations
    for i in range(n):
        # Create the rotated version of the string
        rotated = s[i:] + s[:i]
        # If the rotated string matches the original, return the number of rotations
        if rotated == s:
            return i + 1  # +1 because we want the count of rotations
    
    return n  # In the worst case, it will take n rotations to return to the original

# Test case
assert find_rotations("aaaa") == 1
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_Rotations("aaaa") == 1
    assert find_Rotations("ab") == 2
    assert find_Rotations("abc") == 3
