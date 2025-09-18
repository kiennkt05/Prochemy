# MBPP/533
### Completion
def remove_datatype(input_tuple, data_type):
    return [item for item in input_tuple if not isinstance(item, data_type)]

# Example usage
assert remove_datatype((4, 5, 4, 7.7, 1.2), int) == [7.7, 1.2]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert remove_datatype((4, 5, 4, 7.7, 1.2), int) == [7.7, 1.2]
    assert remove_datatype((7, 8, 9, "SR"), str) == [7, 8, 9]
    assert remove_datatype((7, 1.1, 2, 2.2), float) == [7, 2]
