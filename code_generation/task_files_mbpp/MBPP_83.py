# MBPP/83
### Completion
def get_Char(s):
    # Calculate the sum of ASCII values of all characters in the string
    total = sum(ord(char) for char in s)
    # Convert the total back to a character
    return chr(total)

# Test the function with the provided assertion
assert get_Char("abc") == "f"
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert get_Char("abc") == "f"
    assert get_Char("gfg") == "t"
    assert get_Char("ab") == "c"
