# MBPP/230
### Completion
def replace_blank(input_string: str, replacement_char: str) -> str:
    """
    Replace all blank spaces in the input string with the specified character.

    Parameters:
    input_string (str): The string in which to replace blank spaces.
    replacement_char (str): The character to replace blank spaces with.

    Returns:
    str: The modified string with blank spaces replaced.
    """
    # Replace blank spaces with the specified character
    return input_string.replace(' ', replacement_char)

# Test case
assert replace_blank("hello people", '@') == "hello@people"

# You can add more test cases to validate the function
assert replace_blank("this is a test", '-') == "this-is-a-test"
assert replace_blank("no spaces", '*') == "no*spaces"
assert replace_blank("   leading and trailing   ", '#') == "###leading#and#trailing###"
assert replace_blank("", '$') == ""  # Edge case: empty string
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert replace_blank("hello people",'@')==("hello@people")
    assert replace_blank("python program language",'$')==("python$program$language")
    assert replace_blank("blank space","-")==("blank-space")
