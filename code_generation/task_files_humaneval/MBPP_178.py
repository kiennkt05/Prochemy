# MBPP/178
### Completion
def string_literals(literals, target_string):
    """
    Search for literal strings in a target string.

    Parameters:
    literals (list): A list of strings to search for.
    target_string (str): The string in which to search for the literals.

    Returns:
    str: 'Matched!' if any literal is found in the target string, otherwise 'Not Matched!'.
    """
    # Check if any literal is present in the target string
    for literal in literals:
        if literal in target_string:
            return 'Matched!'
    return 'Not Matched!'

# Test case
assert string_literals(['language'], 'python language') == 'Matched!'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert string_literals(['language'],'python language')==('Matched!')
    assert string_literals(['program'],'python language')==('Not Matched!')
    assert string_literals(['python'],'programming language')==('Not Matched!')
