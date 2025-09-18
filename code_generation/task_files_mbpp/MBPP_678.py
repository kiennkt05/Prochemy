# MBPP/678
### Completion
def remove_spaces(input_string):
    return input_string.replace(" ", "")

# Test the function
assert remove_spaces("a b c") == "abc"
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert remove_spaces("a b c") == "abc"
    assert remove_spaces("1 2 3") == "123"
    assert remove_spaces(" b c") == "bc"
