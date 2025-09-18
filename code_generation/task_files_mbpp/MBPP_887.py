# MBPP/887
### Completion
def is_odd(number):
    return (number & 1) == 1

# Test the function
assert is_odd(5) == True
assert is_odd(4) == False
assert is_odd(0) == False
assert is_odd(-3) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert is_odd(5) == True
    assert is_odd(6) == False
    assert is_odd(7) == True
