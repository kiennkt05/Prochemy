# MBPP/868
### Completion
def length_of_last_word(s: str) -> int:
    # Strip any trailing spaces and split the string into words
    words = s.strip().split()
    # Return the length of the last word if there are any words
    return len(words[-1]) if words else 0

# Test the function with the provided assertion
assert length_of_last_word("python language") == 8
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert length_Of_Last_Word("python language") == 8
    assert length_Of_Last_Word("PHP") == 3
    assert length_Of_Last_Word("") == 0
