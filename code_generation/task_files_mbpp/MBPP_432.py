# MBPP/432
### Completion
def median_trapezium(a, b, c):
    # a and b are the lengths of the two parallel sides
    # c is not used in the median calculation
    return (a + b) / 2

# Test the function with the provided assertion
assert median_trapezium(15, 25, 35) == 20
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert median_trapezium(15,25,35)==20
    assert median_trapezium(10,20,30)==15
    assert median_trapezium(6,9,4)==7.5
