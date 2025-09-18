# MBPP/310
### Completion
def string_to_tuple(s):
    return tuple(s)

# Test the function with the provided assertion
assert string_to_tuple("python 3.0") == ('p', 'y', 't', 'h', 'o', 'n', ' ', '3', '.', '0')
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert string_to_tuple("python 3.0")==('p', 'y', 't', 'h', 'o', 'n', '3', '.', '0')
    assert string_to_tuple("item1")==('i', 't', 'e', 'm', '1')
    assert string_to_tuple("15.10")==('1', '5', '.', '1', '0')
