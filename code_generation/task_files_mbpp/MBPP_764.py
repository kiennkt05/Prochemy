# MBPP/764
### Completion
def number_ctr(s):
    return sum(c.isdigit() for c in s)

# Test the function with the provided assertion
assert number_ctr('program2bedone') == 1
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert number_ctr('program2bedone') == 1
    assert number_ctr('3wonders') ==1
    assert number_ctr('123') == 3
