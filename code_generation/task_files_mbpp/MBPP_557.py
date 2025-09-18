# MBPP/557
### Completion
def toggle_string(s):
    return s.swapcase()

# Test the function
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
