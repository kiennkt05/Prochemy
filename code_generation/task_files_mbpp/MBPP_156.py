# MBPP/156
### Completion
def tuple_int_str(input_tuple):
    return tuple(tuple(int(value) for value in inner_tuple) for inner_tuple in input_tuple)

# Test the function with the provided assertion
assert tuple_int_str((('333', '33'), ('1416', '55'))) == ((333, 33), (1416, 55))
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert tuple_int_str((('333', '33'), ('1416', '55')))==((333, 33), (1416, 55))
    assert tuple_int_str((('999', '99'), ('1000', '500')))==((999, 99), (1000, 500))
    assert tuple_int_str((('666', '66'), ('1500', '555')))==((666, 66), (1500, 555))
