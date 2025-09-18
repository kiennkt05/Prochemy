# MBPP/937
### Completion
from collections import Counter

def max_char(s):
    # Normalize the string to lowercase
    s = s.lower()
    
    # Count the occurrences of each character
    char_count = Counter(s)
    
    # Find the character with the maximum count
    most_common_char = max(char_count, key=char_count.get)
    
    return most_common_char

# Test case
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
