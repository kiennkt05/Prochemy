# MBPP/116
### Completion
def tuple_to_int(tup):
    # Convert each integer in the tuple to a string and join them
    return int(''.join(map(str, tup)))

# Test the function with the provided assertion
assert tuple_to_int((1, 2, 3)) == 123
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert tuple_to_int((1,2,3))==123
    assert tuple_to_int((4,5,6))==456
    assert tuple_to_int((5,6,7))==567
