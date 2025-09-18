# MBPP/893
### Completion
def Extract(sublists):
    return [sublist[-1] for sublist in sublists]

# Test the function with the provided assertion
assert Extract([[1, 2, 3], [4, 5], [6, 7, 8, 9]]) == [3, 5, 9]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert Extract([[1, 2, 3], [4, 5], [6, 7, 8, 9]]) == [3, 5, 9]
    assert Extract([['x', 'y', 'z'], ['m'], ['a', 'b'], ['u', 'v']]) == ['z', 'm', 'b', 'v']
    assert Extract([[1, 2, 3], [4, 5]]) == [3, 5]
