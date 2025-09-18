# MBPP/171
### Completion
def perimeter_pentagon(side_length):
    return 5 * side_length

# Test the function with the provided assertion
assert perimeter_pentagon(5) == 25
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert perimeter_pentagon(5)==25
    assert perimeter_pentagon(10)==50
    assert perimeter_pentagon(15)==75
