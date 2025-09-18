# MBPP/663
### Completion
def find_max_val(x, y, limit):
    if y >= x:
        raise ValueError("y must be less than x for the modulo operation to be valid.")
    
    # Calculate the largest k such that k % x = y
    # k = n * x + y, where n is the largest integer such that k <= limit
    n = (limit - y) // x  # Find the largest n
    k = n * x + y  # Calculate k
    
    return k

# Test the function with the provided assertion
assert find_max_val(15, 10, 5) == 15
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_max_val(15, 10, 5) == 15
    assert find_max_val(187, 10, 5) == 185
    assert find_max_val(16, 11, 1) == 12
