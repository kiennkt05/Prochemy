# MBPP/800
### Completion
def remove_all_spaces(input_string):
    return input_string.replace(" ", "")

# Test the function
assert remove_all_spaces('python  program') == 'pythonprogram'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert remove_all_spaces('python  program')==('pythonprogram')
    assert remove_all_spaces('python   programming    language')==('pythonprogramminglanguage')
    assert remove_all_spaces('python                     program')==('pythonprogram')
