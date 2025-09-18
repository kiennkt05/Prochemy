# MBPP/259
### Completion
def maximize_elements(tuple1, tuple2):
    # Use a list comprehension to create a new tuple with the maximum values
    return tuple((max(a, b) for a, b in zip(t1, t2)) for t1, t2 in zip(tuple1, tuple2))

# Test the function with the provided assertion
assert maximize_elements(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3))) == ((6, 7), (4, 9), (2, 9), (7, 10))

# If the assertion passes, the function works as expected.
print("Function works correctly.")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert maximize_elements(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3))) == ((6, 7), (4, 9), (2, 9), (7, 10))
    assert maximize_elements(((2, 4), (5, 6), (3, 10), (2, 11)), ((7, 8), (4, 10), (2, 2), (8, 4))) == ((7, 8), (5, 10), (3, 10), (8, 11))
    assert maximize_elements(((3, 5), (6, 7), (4, 11), (3, 12)), ((8, 9), (5, 11), (3, 3), (9, 5))) == ((8, 9), (6, 11), (4, 11), (9, 12))
