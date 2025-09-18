# MBPP/48
### Completion
def odd_bit_set_number(n):
    # Create a mask with all odd bits set (0b01010101)
    mask = 0b01010101
    # Set all odd bits of the given number using bitwise OR
    return n | mask

# Test the function with the provided assertion
assert odd_bit_set_number(10) == 15

# You can also print the result to verify
print(odd_bit_set_number(10))  # Output should be 15
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert odd_bit_set_number(10) == 15
    assert odd_bit_set_number(20) == 21
    assert odd_bit_set_number(30) == 31
