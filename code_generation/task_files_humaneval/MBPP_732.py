# MBPP/732
### Completion
def replace_specialchar(input_string):
    """
    Replace all occurrences of spaces, commas, or dots in the input string with a colon.

    Parameters:
    input_string (str): The string in which to replace characters.

    Returns:
    str: The modified string with specified characters replaced by colons.
    """
    # Replace spaces, commas, and dots with colons
    modified_string = input_string.replace(' ', ':').replace(',', ':').replace('.', ':')
    return modified_string

# Test case
assert replace_specialchar('Python language, Programming language.') == 'Python:language::Programming:language:'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert replace_specialchar('Python language, Programming language.')==('Python:language::Programming:language:')
    assert replace_specialchar('a b c,d e f')==('a:b:c:d:e:f')
    assert replace_specialchar('ram reshma,ram rahim')==('ram:reshma:ram:rahim')
