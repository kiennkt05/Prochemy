# MBPP/238
### Completion
def number_of_substrings(s: str) -> int:
    n = len(s)
    return n * (n + 1) // 2

# Test the function with the provided assertion
assert number_of_substrings("abc") == 6
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert number_of_substrings("abc") == 6
    assert number_of_substrings("abcd") == 10
    assert number_of_substrings("abcde") == 15
