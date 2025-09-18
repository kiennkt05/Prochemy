# MBPP/929
### Completion
def count_tuplex(tup, item):
    return tup.count(item)

# Test the function with the provided assertion
assert count_tuplex((2, 4, 5, 6, 2, 3, 4, 4, 7), 4) == 3
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_tuplex((2, 4, 5, 6, 2, 3, 4, 4, 7),4)==3
    assert count_tuplex((2, 4, 5, 6, 2, 3, 4, 4, 7),2)==2
    assert count_tuplex((2, 4, 7, 7, 7, 3, 4, 4, 7),7)==4
