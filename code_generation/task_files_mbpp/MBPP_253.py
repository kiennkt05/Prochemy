# MBPP/253
### Completion
def count_integer(lst):
    return sum(1 for item in lst if isinstance(item, int))

# Test the function with the provided assertion
assert count_integer([1, 2, 'abc', 1.2]) == 2
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_integer([1,2,'abc',1.2]) == 2
    assert count_integer([1,2,3]) == 3
    assert count_integer([1,1.2,4,5.1]) == 2
