# MBPP/651
### Completion
def check_subset(tuple1, tuple2):
    # Convert tuples to sets and check if tuple2 is a subset of tuple1
    return set(tuple2).issubset(set(tuple1))

# Test the function with the provided assertion
assert check_subset((10, 4, 5, 6), (5, 10)) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_subset((10, 4, 5, 6), (5, 10)) == True
    assert check_subset((1, 2, 3, 4), (5, 6)) == False
    assert check_subset((7, 8, 9, 10), (10, 8)) == True
