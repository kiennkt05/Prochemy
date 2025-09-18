# MBPP/965
### Completion
def camel_to_snake(camel_str):
    """
    Convert a camel case string to a snake case string.

    Parameters:
    camel_str (str): The camel case string to convert.

    Returns:
    str: The converted snake case string.
    """
    snake_str = []
    
    for char in camel_str:
        if char.isupper():
            # If it's not the first character, prepend an underscore
            if snake_str:
                snake_str.append('_')
            # Convert to lowercase and add to the result
            snake_str.append(char.lower())
        else:
            # Just add the lowercase character
            snake_str.append(char)
    
    return ''.join(snake_str)

# Test case
assert camel_to_snake('PythonProgram') == 'python_program'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert camel_to_snake('PythonProgram')==('python_program')
    assert camel_to_snake('pythonLanguage')==('python_language')
    assert camel_to_snake('ProgrammingLanguage')==('programming_language')
