# MBPP/945
### Completion
def tuple_to_set(input_tuple):
    return set(input_tuple)

# Test the function with the provided assertion
assert tuple_to_set(('x', 'y', 'z')) == {'y', 'x', 'z'}
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert tuple_to_set(('x', 'y', 'z') ) == {'y', 'x', 'z'}
    assert tuple_to_set(('a', 'b', 'c') ) == {'c', 'a', 'b'}
    assert tuple_to_set(('z', 'd', 'e') ) == {'d', 'e', 'z'}
