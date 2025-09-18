# MBPP/913
### Completion
def end_num(s):
    # Check if the last character of the string is a digit
    return s[-1].isdigit() if s else False

# Test the function with the provided assertion
assert end_num('abcdef') == False
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert end_num('abcdef')==False
    assert end_num('abcdef7')==True
    assert end_num('abc')==False
