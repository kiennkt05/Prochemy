# MBPP/568
### Completion
def empty_list(n):
    return [{} for _ in range(n)]

# Test the function with the provided assertion
assert empty_list(5) == [{}, {}, {}, {}, {}]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert empty_list(5)==[{},{},{},{},{}]
    assert empty_list(6)==[{},{},{},{},{},{}]
    assert empty_list(7)==[{},{},{},{},{},{},{}]
