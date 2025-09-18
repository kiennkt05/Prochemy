# MBPP/750
### Completion
def add_tuple(lst, tup):
    # Convert the tuple to a list and extend the original list with it
    lst.extend(tup)
    return lst

# Test the function with the provided assertion
assert add_tuple([5, 6, 7], (9, 10)) == [5, 6, 7, 9, 10]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert add_tuple([5, 6, 7], (9, 10)) == [5, 6, 7, 9, 10]
    assert add_tuple([6, 7, 8], (10, 11)) == [6, 7, 8, 10, 11]
    assert add_tuple([7, 8, 9], (11, 12)) == [7, 8, 9, 11, 12]
