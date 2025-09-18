# MBPP/925
### Completion
def multiple_tuple(numbers):
    product = 1
    for number in numbers:
        product *= number
    return product

# Test the function with the provided assertion
assert multiple_tuple((4, 3, 2, 2, -1, 18)) == -864
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert mutiple_tuple((4, 3, 2, 2, -1, 18)) == -864
    assert mutiple_tuple((1,2,3)) == 6
    assert mutiple_tuple((-2,-4,-6)) == -48
