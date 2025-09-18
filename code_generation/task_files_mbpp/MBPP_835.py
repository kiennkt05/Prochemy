# MBPP/835
### Completion
def slope(x1, y1, x2, y2):
    if x2 - x1 == 0:  # Check for division by zero
        raise ValueError("The x-coordinates must be different to calculate the slope.")
    return (y2 - y1) / (x2 - x1)

# Test the function with the provided assertion
assert slope(4, 2, 2, 5) == -1.5
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert slope(4,2,2,5) == -1.5
    assert slope(2,4,4,6) == 1
    assert slope(1,2,4,2) == 0
