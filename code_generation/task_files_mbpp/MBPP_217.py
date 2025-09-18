# MBPP/217
### Completion
def first_Repeated_Char(s):
    seen = set()
    for char in s:
        if char in seen:
            return char
        seen.add(char)
    return None  # Return None if there are no repeated characters

# Test the function with the provided assertion
assert first_Repeated_Char("Google") == "o"
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert first_Repeated_Char("Google") == "o"
    assert first_Repeated_Char("data") == "a"
    assert first_Repeated_Char("python") == '\0'
