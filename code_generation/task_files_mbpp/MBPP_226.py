# MBPP/226
### Completion
def odd_values_string(s):
    return ''.join(s[i] for i in range(len(s)) if i % 2 == 0)

# Test the function with the provided assertion
assert odd_values_string('abcdef') == 'ace'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert odd_values_string('abcdef') == 'ace'
    assert odd_values_string('python') == 'pto'
    assert odd_values_string('data') == 'dt'
