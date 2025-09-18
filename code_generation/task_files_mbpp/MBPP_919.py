# MBPP/919
### Completion
def multiply_list(items):
    result = 1
    for item in items:
        result *= item
    return result

# Test the function with the provided assertion
assert multiply_list([1, -2, 3]) == -6
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert multiply_list([1,-2,3]) == -6
    assert multiply_list([1,2,3,4]) == 24
    assert multiply_list([3,1,2,3]) == 18
