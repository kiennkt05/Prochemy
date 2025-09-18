# MBPP/235
### Completion
def even_bit_set_number(n):
    # Create a mask with all even bits set to 1
    mask = 0b01010101010101010101010101010101  # This is 0xAAAAAAAA in hexadecimal
    # Use bitwise OR to set the even bits of n
    return n | mask

# Test the function with the provided assertion
assert even_bit_set_number(10) == 10
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert even_bit_set_number(10) == 10
    assert even_bit_set_number(20) == 30
    assert even_bit_set_number(30) == 30
