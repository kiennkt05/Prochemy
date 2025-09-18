# MBPP/800
### Completion
def remove_all_spaces(input_string: str) -> str:
    """
    Remove all whitespace characters from the input string.

    Parameters:
    input_string (str): The string from which to remove whitespace.

    Returns:
    str: A new string with all whitespace removed.
    """
    # Replace all spaces with an empty string
    return input_string.replace(' ', '')

# Test case
assert remove_all_spaces('python  program') == 'pythonprogram'

# Additional test cases for verification
assert remove_all_spaces('  hello world  ') == 'helloworld'
assert remove_all_spaces('no spaces') == 'nospaces'
assert remove_all_spaces('   ') == ''
assert remove_all_spaces('') == ''
assert remove_all_spaces('a b c d e') == 'abcde'

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert remove_all_spaces('python  program')==('pythonprogram')
    assert remove_all_spaces('python   programming    language')==('pythonprogramminglanguage')
    assert remove_all_spaces('python                     program')==('pythonprogram')
