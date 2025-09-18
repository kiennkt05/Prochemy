# MBPP/146
### Completion
def ascii_value_string(s):
    return sum(ord(char) for char in s)

# Test the function with the provided assertion
assert ascii_value_string("python") == 112
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert ascii_value_string("python")==112
    assert ascii_value_string("Program")==80
    assert ascii_value_string("Language")==76
