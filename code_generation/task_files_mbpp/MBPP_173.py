# MBPP/173
### Completion
import re

def remove_splchar(input_string):
    # Use regular expression to remove non-alphanumeric characters
    return re.sub(r'[^a-zA-Z0-9]', '', input_string)

# Test the function with the provided assertion
assert remove_splchar('python  @#&^%$*program123') == 'pythonprogram123'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert remove_splchar('python  @#&^%$*program123')==('pythonprogram123')
    assert remove_splchar('python %^$@!^&*()  programming24%$^^()    language')==('pythonprogramming24language')
    assert remove_splchar('python   ^%&^()(+_)(_^&67)                  program')==('python67program')
