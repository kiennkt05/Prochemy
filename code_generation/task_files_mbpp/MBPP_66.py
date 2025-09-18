# MBPP/66
### Completion
def pos_count(numbers):
    """Count the number of positive numbers in a list."""
    return sum(1 for num in numbers if num > 0)

# Test the function with the provided assertion
assert pos_count([1, -2, 3, -4]) == 2
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert pos_count([1,-2,3,-4]) == 2
    assert pos_count([3,4,5,-1]) == 3
    assert pos_count([1,2,3,4]) == 4
