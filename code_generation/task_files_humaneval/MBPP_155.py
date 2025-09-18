# MBPP/155
### Completion
def even_bit_toggle_number(n):
    # Create a mask with 1s in all even bit positions
    mask = 0
    for i in range(32):  # Assuming we are working with a 32-bit integer
        if i % 2 == 0:  # Check if the bit position is even
            mask |= (1 << i)  # Set the bit at position i in the mask

    # Toggle the even bits of the number using XOR
    result = n ^ mask
    return result

# Test case
assert even_bit_toggle_number(10) == 0  # 10 in binary is 1010, toggling even bits gives 0000
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert even_bit_toggle_number(10) == 0
    assert even_bit_toggle_number(20) == 30
    assert even_bit_toggle_number(30) == 20
