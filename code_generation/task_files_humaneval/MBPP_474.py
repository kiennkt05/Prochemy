# MBPP/474
### Completion
def replace_char(original: str, to_replace: str, replacement: str) -> str:
    """
    Replace all occurrences of a specified character in a string with another character.

    Parameters:
    original (str): The original string in which characters will be replaced.
    to_replace (str): The character that needs to be replaced.
    replacement (str): The character that will replace the 'to_replace' character.

    Returns:
    str: The modified string with characters replaced.
    """
    # Use the str.replace() method to replace the characters
    return original.replace(to_replace, replacement)

# Test case
assert replace_char("polygon", 'y', 'l') == "pollgon"

# If you want to see the output of the test case, you can uncomment the following line:
# print(replace_char("polygon", 'y', 'l'))  # This should print "pollgon"
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert replace_char("polygon",'y','l')==("pollgon")
    assert replace_char("character",'c','a')==("aharaater")
    assert replace_char("python",'l','a')==("python")
