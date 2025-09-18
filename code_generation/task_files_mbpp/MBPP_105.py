# MBPP/105
### Completion
def count(boolean_list):
    return sum(1 for value in boolean_list if value is True)

# Test the function with the provided assertion
assert count([True, False, True]) == 2
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count([True,False,True]) == 2
    assert count([False,False]) == 0
    assert count([True,True,True]) == 3
