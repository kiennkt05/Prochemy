# MBPP/349
### Completion
def check(s):
    # Check if all characters in the string are either '0' or '1'
    if all(char in '01' for char in s):
        return "Yes"
    else:
        return "No"

# Test the function with the provided assertion
assert check("01010101010") == "Yes"
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check("01010101010") == "Yes"
    assert check("name0") == "No"
    assert check("101") == "Yes"
