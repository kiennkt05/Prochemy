# MBPP/602
### Completion
def first_repeated_char(s):
    seen = set()
    for char in s:
        if char in seen:
            return char
        seen.add(char)
    return None  # Return None if there are no repeated characters

# Test the function with the provided assertion
assert first_repeated_char("abcabc") == "a"
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert first_repeated_char("abcabc") == "a"
    assert first_repeated_char("abc") == "None"
    assert first_repeated_char("123123") == "1"
