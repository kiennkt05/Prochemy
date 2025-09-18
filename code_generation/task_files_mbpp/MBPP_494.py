# MBPP/494
### Completion
def binary_to_integer(binary_tuple):
    # Convert the tuple to a string and then to an integer using base 2
    binary_string = ''.join(str(bit) for bit in binary_tuple)
    integer_value = int(binary_string, 2)
    return str(integer_value)

# Test the function with the provided assertion
assert binary_to_integer((1, 1, 0, 1, 0, 0, 1)) == '105'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert binary_to_integer((1, 1, 0, 1, 0, 0, 1)) == '105'
    assert binary_to_integer((0, 1, 1, 0, 0, 1, 0, 1)) == '101'
    assert binary_to_integer((1, 1, 0, 1, 0, 1)) == '53'
