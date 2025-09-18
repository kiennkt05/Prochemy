# MBPP/203
### Completion
def hamming_distance(x, y):
    # XOR the two numbers and count the number of 1s in the result
    return bin(x ^ y).count('1')

# Test the function with the provided assertion
assert hamming_distance(4, 8) == 2

# You can also add some additional test cases if needed
print(hamming_distance(4, 8))  # Output: 2
print(hamming_distance(1, 4))  # Output: 2
print(hamming_distance(0, 0))  # Output: 0
print(hamming_distance(15, 8)) # Output: 4
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert hamming_Distance(4,8) == 2
    assert hamming_Distance(2,4) == 2
    assert hamming_Distance(1,2) == 2
