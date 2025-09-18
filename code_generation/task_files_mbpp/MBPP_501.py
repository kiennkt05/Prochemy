# MBPP/501
### Completion
def num_comm_div(a, b):
    """Return the greatest common divisor of a and b."""
    while b:
        a, b = b, a % b
    return a

# Test the function with the provided assertion
assert num_comm_div(2, 4) == 2
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert num_comm_div(2,4) == 2
    assert num_comm_div(2,8) == 2
    assert num_comm_div(12,24) == 6
