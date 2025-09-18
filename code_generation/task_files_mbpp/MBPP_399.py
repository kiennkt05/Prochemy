# MBPP/399
### Completion
def bitwise_xor(tuple1, tuple2):
    # Use a generator expression to apply the XOR operation on corresponding elements
    return tuple(a ^ b for a, b in zip(tuple1, tuple2))

# Test the function with the provided assertion
assert bitwise_xor((10, 4, 6, 9), (5, 2, 3, 3)) == (15, 6, 5, 10)

# You can also print the result to verify
print(bitwise_xor((10, 4, 6, 9), (5, 2, 3, 3)))  # Output: (15, 6, 5, 10)
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert bitwise_xor((10, 4, 6, 9), (5, 2, 3, 3)) == (15, 6, 5, 10)
    assert bitwise_xor((11, 5, 7, 10), (6, 3, 4, 4)) == (13, 6, 3, 14)
    assert bitwise_xor((12, 6, 8, 11), (7, 4, 5, 6)) == (11, 2, 13, 13)
