# MBPP/470
### Completion
def add_pairwise(tup):
    # Use a list comprehension to sum pairs of elements
    return tuple(tup[i] + tup[i + 1] for i in range(len(tup) - 1))

# Test the function with the provided assertion
assert add_pairwise((1, 5, 7, 8, 10)) == (6, 12, 15, 18)

# You can also print the result to verify
print(add_pairwise((1, 5, 7, 8, 10)))  # Output: (6, 12, 15, 18)
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert add_pairwise((1, 5, 7, 8, 10)) == (6, 12, 15, 18)
    assert add_pairwise((2, 6, 8, 9, 11)) == (8, 14, 17, 20)
    assert add_pairwise((3, 7, 9, 10, 12)) == (10, 16, 19, 22)
