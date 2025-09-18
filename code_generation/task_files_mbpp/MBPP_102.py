# MBPP/102
### Completion
def snake_to_camel(snake_str):
    # Split the string by underscores
    components = snake_str.split('_')
    # Capitalize the first letter of each component and join them
    camel_case_str = ''.join(x.capitalize() for x in components)
    return camel_case_str

# Test the function
assert snake_to_camel('python_program') == 'PythonProgram'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert snake_to_camel('python_program')=='PythonProgram'
    assert snake_to_camel('python_language')==('PythonLanguage')
    assert snake_to_camel('programming_language')==('ProgrammingLanguage')
