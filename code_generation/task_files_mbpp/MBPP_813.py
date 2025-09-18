# MBPP/813
### Completion
def string_length(s):
    return len(s)

# Test the function
assert string_length('python') == 6
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert string_length('python')==6
    assert string_length('program')==7
    assert string_length('language')==8
