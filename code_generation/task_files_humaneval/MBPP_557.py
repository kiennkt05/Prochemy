# MBPP/557
### Completion
def toggle_string(s: str) -> str:
    """
    Toggle the case of each character in the input string.

    Parameters:
    s (str): The input string whose characters' cases are to be toggled.

    Returns:
    str: A new string with the case of each character toggled.
    """
    # Using a list comprehension to toggle the case of each character
    toggled = ''.join(char.lower() if char.isupper() else char.upper() for char in s)
    return toggled

# Test case
assert toggle_string("Python") == "pYTHON"
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert toggle_string("Python")==("pYTHON")
    assert toggle_string("Pangram")==("pANGRAM")
    assert toggle_string("LIttLE")==("liTTle")
