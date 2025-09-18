# MBPP/44
### Completion
def text_match_string(input_string):
    if input_string.startswith("python"):
        return "Matched!"
    else:
        return "Not matched!"

# Test the function
assert text_match_string(" python") == 'Not matched!'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert text_match_string(" python")==('Not matched!')
    assert text_match_string("python")==('Found a match!')
    assert text_match_string("  lang")==('Not matched!')
