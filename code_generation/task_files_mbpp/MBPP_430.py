# MBPP/430
### Completion
def parabola_directrix(a, h, k):
    # Calculate p
    p = 1 / (4 * a)
    # Calculate the directrix
    directrix = k - p
    return directrix

# Test the function with the provided assertion
assert parabola_directrix(5, 3, 2) == -198
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert parabola_directrix(5,3,2)==-198
    assert parabola_directrix(9,8,4)==-2336
    assert parabola_directrix(2,4,6)==-130
