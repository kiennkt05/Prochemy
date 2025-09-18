# MBPP/118
### Completion
def string_to_list(input_string):
    # Split the string by spaces and return the list
    return input_string.split()

# Test the function with the provided assertion
assert string_to_list("python programming") == ['python', 'programming']
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert string_to_list("python programming")==['python','programming']
    assert string_to_list("lists tuples strings")==['lists','tuples','strings']
    assert string_to_list("write a program")==['write','a','program']
