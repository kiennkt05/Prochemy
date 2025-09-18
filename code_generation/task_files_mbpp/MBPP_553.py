# MBPP/553
### Completion
def tuple_to_float(tup):
    # Convert the tuple to a string and replace the comma with a dot
    float_str = ''.join(map(str, tup)).replace(',', '.')
    # Convert the string to a float
    return float(float_str)

# Test the function
assert tuple_to_float((4, 56)) == 4.56
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert tuple_to_float((4, 56)) == 4.56
    assert tuple_to_float((7, 256)) == 7.256
    assert tuple_to_float((8, 123)) == 8.123
