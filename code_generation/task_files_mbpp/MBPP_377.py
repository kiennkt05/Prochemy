# MBPP/377
### Completion
def remove_Char(s, char):
    return s.replace(char, '')

# Test the function with the provided assertion
assert remove_Char("aba", 'a') == "b"
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert remove_Char("aba",'a') == "b"
    assert remove_Char("toggle",'g') == "tole"
    assert remove_Char("aabbc",'b') == "aac"
