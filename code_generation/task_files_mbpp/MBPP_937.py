# MBPP/937
### Completion
from collections import Counter

def max_char(s):
    # Count the occurrences of each character in the string
    char_count = Counter(s)
    # Find the character with the maximum count
    most_common_char = char_count.most_common(1)[0][0]
    return most_common_char

# Test the function with the provided assertion
assert max_char("hello world") == 'l'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert max_char("hello world")==('l')
    assert max_char("hello ")==('l')
    assert max_char("python pr")==('p')
