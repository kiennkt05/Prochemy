# MBPP/538
### Completion
def string_list_to_tuple(input_string):
    # Convert the string to a tuple of its characters
    return tuple(input_string)

# Test the function with the provided assertion
assert string_list_to_tuple("python 3.0") == ('p', 'y', 't', 'h', 'o', 'n', ' ', '3', '.', '0')
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert string_list_to_tuple(("python 3.0")) == ('p', 'y', 't', 'h', 'o', 'n', '3', '.', '0')
    assert string_list_to_tuple(("bigdata")) == ('b', 'i', 'g', 'd', 'a', 't', 'a')
    assert string_list_to_tuple(("language")) == ('l', 'a', 'n', 'g', 'u', 'a', 'g','e')
