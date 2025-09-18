# MBPP/478
### Completion
def remove_lowercase(s):
    # Use a list comprehension to filter out lowercase characters
    result = ''.join([char for char in s if not char.islower()])
    return result

# Test the function with the provided assertion
assert remove_lowercase("PYTHon") == 'PYTH'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert remove_lowercase("PYTHon")==('PYTH')
    assert remove_lowercase("FInD")==('FID')
    assert remove_lowercase("STRinG")==('STRG')
