# MBPP/715
### Completion
def str_to_tuple(s):
    # Split the string by commas and convert each part to an integer
    return tuple(int(num.strip()) for num in s.split(','))

# Test the function with the provided assertion
assert str_to_tuple("1, -5, 4, 6, 7") == (1, -5, 4, 6, 7)
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert str_to_tuple("1, -5, 4, 6, 7") == (1, -5, 4, 6, 7)
    assert str_to_tuple("1, 2, 3, 4, 5") == (1, 2, 3, 4, 5)
    assert str_to_tuple("4, 6, 9, 11, 13, 14") == (4, 6, 9, 11, 13, 14)
