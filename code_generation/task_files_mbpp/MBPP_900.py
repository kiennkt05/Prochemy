# MBPP/900
### Completion
def match_num(s):
    # Check if the string starts with '5'
    return s.startswith('5')

# Test the function with the provided assertion
assert match_num('5-2345861') == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert match_num('5-2345861')==True
    assert match_num('6-2345861')==False
    assert match_num('78910')==False
