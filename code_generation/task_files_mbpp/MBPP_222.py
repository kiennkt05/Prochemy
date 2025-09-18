# MBPP/222
### Completion
def check_type(tup):
    if not tup:  # Check if the tuple is empty
        return True
    first_type = type(tup[0])  # Get the type of the first element
    return all(isinstance(item, first_type) for item in tup)  # Check if all elements are of the same type

# Test the function with the provided assertion
assert check_type((5, 6, 7, 3, 5, 6)) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_type((5, 6, 7, 3, 5, 6) ) == True
    assert check_type((1, 2, "4") ) == False
    assert check_type((3, 2, 1, 4, 5) ) == True
