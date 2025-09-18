# MBPP/102
### Completion
def snake_to_camel(snake_str):
    """
    Convert a snake case string to camel case string.

    Parameters:
    snake_str (str): The input string in snake case.

    Returns:
    str: The converted string in camel case.
    """
    # Split the string by underscores
    words = snake_str.split('_')
    
    # Capitalize the first letter of each word and join them
    camel_case_str = ''.join(word.capitalize() for word in words)
    
    return camel_case_str

# Test case
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
