# MBPP/113
### Completion
def check_integer(s):
    # Check if the string can be converted to an integer
    try:
        int(s)
        return True
    except ValueError:
        return False

# Test cases
assert check_integer("python") == False
assert check_integer("123") == True
assert check_integer("-456") == True
assert check_integer("3.14") == False
assert check_integer("0") == True
assert check_integer("") == False
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_integer("python")==False
    assert check_integer("1")==True
    assert check_integer("12345")==True
