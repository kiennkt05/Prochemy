# MBPP/17
### Completion
def square_perimeter(side_length):
    return 4 * side_length

# Test the function with the provided assertion
assert square_perimeter(10) == 40
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert square_perimeter(10)==40
    assert square_perimeter(5)==20
    assert square_perimeter(4)==16
