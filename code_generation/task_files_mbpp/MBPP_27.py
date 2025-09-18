# MBPP/27
### Completion
def remove(strings):
    return [''.join(filter(lambda x: not x.isdigit(), s)) for s in strings]

# Test the function with the provided assertion
assert remove(['4words', '3letters', '4digits']) == ['words', 'letters', 'digits']
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert remove(['4words', '3letters', '4digits']) == ['words', 'letters', 'digits']
    assert remove(['28Jan','12Jan','11Jan']) == ['Jan','Jan','Jan']
    assert remove(['wonder1','wonder2','wonder3']) == ['wonder','wonder','wonder']
