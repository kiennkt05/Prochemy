# MBPP/713
### Completion
def check_valid(tup):
    # Check if all elements in the tuple are boolean values
    return all(isinstance(x, bool) for x in tup)

# Test the function with the provided assertion
assert check_valid((True, True, True, True)) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_valid((True, True, True, True) ) == True
    assert check_valid((True, False, True, True) ) == False
    assert check_valid((True, True, True, True) ) == True
