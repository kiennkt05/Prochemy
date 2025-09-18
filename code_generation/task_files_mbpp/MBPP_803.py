# MBPP/803
### Completion
def is_Perfect_Square(num):
    if num < 0:
        return False
    root = int(num**0.5)
    return root * root == num

# Test the function with the provided assertion
assert is_Perfect_Square(10) == False
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert is_Perfect_Square(10) == False
    assert is_Perfect_Square(36) == True
    assert is_Perfect_Square(14) == False
