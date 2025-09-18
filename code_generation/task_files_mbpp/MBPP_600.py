# MBPP/600
### Completion
def is_Even(number):
    return (number & 1) == 0

# Test the function with the provided assertion
assert is_Even(1) == False
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert is_Even(1) == False
    assert is_Even(2) == True
    assert is_Even(3) == False
