# MBPP/355
### Completion
def count_Rectangles(r):
    # The number of rectangles that can be inscribed in a circle of radius r
    return 4 * r * r

# Test the function with the provided assertion
assert count_Rectangles(2) == 8
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_Rectangles(2) == 8
    assert count_Rectangles(1) == 1
    assert count_Rectangles(0) == 0
