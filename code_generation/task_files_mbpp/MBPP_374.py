# MBPP/374
### Completion
from itertools import permutations

def permute_string(s):
    # Generate all permutations using itertools.permutations
    perm = permutations(s)
    # Convert the permutations from tuples to strings and return as a list
    return [''.join(p) for p in perm]

# Test the function with the provided assertion
assert permute_string('ab') == ['ab', 'ba']
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert permute_string('ab')==['ab', 'ba']
    assert permute_string('abc')==['abc', 'bac', 'bca', 'acb', 'cab', 'cba']
    assert permute_string('abcd')==['abcd', 'bacd', 'bcad', 'bcda', 'acbd', 'cabd', 'cbad', 'cbda', 'acdb', 'cadb', 'cdab', 'cdba', 'abdc', 'badc', 'bdac', 'bdca', 'adbc', 'dabc', 'dbac', 'dbca', 'adcb', 'dacb', 'dcab', 'dcba']
