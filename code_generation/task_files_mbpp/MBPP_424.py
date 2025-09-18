# MBPP/424
### Completion
def extract_rear(strings):
    return [s[-1] for s in strings]

# Test the function with the provided assertion
assert extract_rear(('Mers', 'for', 'Vers')) == ['s', 'r', 's']
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert extract_rear(('Mers', 'for', 'Vers') ) == ['s', 'r', 's']
    assert extract_rear(('Avenge', 'for', 'People') ) == ['e', 'r', 'e']
    assert extract_rear(('Gotta', 'get', 'go') ) == ['a', 't', 'o']
