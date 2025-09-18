# MBPP/329
### Completion
def neg_count(numbers):
    return sum(1 for num in numbers if num < 0)

# Test the function with the provided assertion
assert neg_count([-1, -2, 3, -4, -5]) == 4
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert neg_count([-1,-2,3,-4,-5]) == 4
    assert neg_count([1,2,3]) == 0
    assert neg_count([1,2,-3,-10,20]) == 2
