# MBPP/269
### Completion
def ascii_value(char):
    return ord(char)

# Test the function with the provided assertion
assert ascii_value('A') == 65
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert ascii_value('A')==65
    assert ascii_value('R')==82
    assert ascii_value('S')==83
