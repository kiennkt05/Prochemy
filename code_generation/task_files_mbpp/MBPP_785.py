# MBPP/785
### Completion
def tuple_str_int(tuple_str):
    # Remove the parentheses and split the string by comma
    elements = tuple_str.strip("()").split(",")
    # Convert each element to an integer and return as a tuple
    return tuple(int(element.strip()) for element in elements)

# Test the function with the provided assertion
assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)
    assert tuple_str_int("(1, 2, 3)") == (1, 2, 3)
    assert tuple_str_int("(4, 5, 6)") == (4, 5, 6)
