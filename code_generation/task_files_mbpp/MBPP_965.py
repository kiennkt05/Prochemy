# MBPP/965
### Completion
def camel_to_snake(camel_str):
    # Initialize an empty list to hold the characters
    snake_str = []
    
    for char in camel_str:
        # If the character is uppercase, add an underscore before it (if it's not the first character)
        if char.isupper() and snake_str:
            snake_str.append('_')
        # Append the lowercase version of the character
        snake_str.append(char.lower())
    
    # Join the list into a string and return
    return ''.join(snake_str)

# Test the function
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
