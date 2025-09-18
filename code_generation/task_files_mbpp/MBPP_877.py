# MBPP/877
### Completion
def sort_String(s):
    return ''.join(sorted(s))

# Test the function
assert sort_String("cba") == "abc"
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sort_String("cba") == "abc"
    assert sort_String("data") == "aadt"
    assert sort_String("zxy") == "xyz"
