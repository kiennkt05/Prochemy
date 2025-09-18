# MBPP/878
### Completion
def check_tuples(tup, elements):
    # Convert the list of elements to a set for faster lookup
    element_set = set(elements)
    
    # Check if all elements in the tuple are in the set of specified elements
    return all(item in element_set for item in tup)

# Test the function with the provided assertion
assert check_tuples((3, 5, 6, 5, 3, 6), [3, 6, 5]) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_tuples((3, 5, 6, 5, 3, 6),[3, 6, 5]) == True
    assert check_tuples((4, 5, 6, 4, 6, 5),[4, 5, 6]) == True
    assert check_tuples((9, 8, 7, 6, 8, 9),[9, 8, 1]) == False
