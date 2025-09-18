# MBPP/150
### Completion
def does_Contain_B(a, b, n):
    if n < a:
        return False
    return (n - a) % b == 0

# Test the function with the provided assertion
assert does_Contain_B(1, 7, 3) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert does_Contain_B(1,7,3) == True
    assert does_Contain_B(1,-3,5) == False
    assert does_Contain_B(3,2,5) == False
