# MBPP/394
### Completion
def check_distinct(tup):
    # Convert the tuple to a set to remove duplicates
    return len(tup) == len(set(tup))

# Test the function with the provided assertion
assert check_distinct((1, 4, 5, 6, 1, 4)) == False
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_distinct((1, 4, 5, 6, 1, 4)) == False
    assert check_distinct((1, 4, 5, 6)) == True
    assert check_distinct((2, 3, 4, 5, 6)) == True
