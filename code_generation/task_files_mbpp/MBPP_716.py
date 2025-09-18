# MBPP/716
### Completion
def rombus_perimeter(side_length):
    return 4 * side_length

# Test the function with the provided assertion
assert rombus_perimeter(10) == 40
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert rombus_perimeter(10)==40
    assert rombus_perimeter(5)==20
    assert rombus_perimeter(4)==16
