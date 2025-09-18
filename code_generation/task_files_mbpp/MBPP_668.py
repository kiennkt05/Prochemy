# MBPP/668
### Completion
def replace(string, char):
    # Replace multiple occurrences of 'char' with a single 'char'
    return ''.join(char if c == char and (i == 0 or string[i-1] != char) else c for i, c in enumerate(string))

# Test the function with the provided assertion
assert replace('peep', 'e') == 'pep'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert replace('peep','e') == 'pep'
    assert replace('Greek','e') == 'Grek'
    assert replace('Moon','o') == 'Mon'
