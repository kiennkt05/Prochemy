# MBPP/892
### Completion
def remove_spaces(input_string):
    # Split the string by whitespace and join it back with a single space
    return ' '.join(input_string.split())

# Test the function with the provided assertion
assert remove_spaces('python  program') == 'python program'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert remove_spaces('python  program')==('python program')
    assert remove_spaces('python   programming    language')==('python programming language')
    assert remove_spaces('python                     program')==('python program')
