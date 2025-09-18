# MBPP/9
### Completion
def find_Rotations(s: str) -> int:
    # Length of the string
    n = len(s)
    
    # If the string is empty or has only one character, it requires 1 rotation
    if n <= 1:
        return 1
    
    # Check for the minimum number of rotations
    for i in range(1, n + 1):
        # Create the rotated version of the string
        rotated = s[i % n:] + s[:i % n]
        if rotated == s:
            return i
    
    return n  # In the worst case, it will take n rotations to return to the original string

# Test the function with the provided assertion
assert find_Rotations("aaaa") == 1
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_Rotations("aaaa") == 1
    assert find_Rotations("ab") == 2
    assert find_Rotations("abc") == 3
