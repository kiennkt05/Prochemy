# MBPP/192
### Completion
def check_String(s):
    has_letter = any(c.isalpha() for c in s)
    has_number = any(c.isdigit() for c in s)
    return has_letter and has_number

# Test the function with the provided assertion
assert check_String('thishasboth29') == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_String('thishasboth29') == True
    assert check_String('python') == False
    assert check_String ('string') == False
