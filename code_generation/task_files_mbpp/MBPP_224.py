# MBPP/224
### Completion
def count_Set_Bits(n):
    count = 0
    while n:
        count += n & 1  # Increment count if the last bit is 1
        n >>= 1         # Right shift n by 1 to check the next bit
    return count

# Test the function with the provided assertion
assert count_Set_Bits(2) == 1
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_Set_Bits(2) == 1
    assert count_Set_Bits(4) == 1
    assert count_Set_Bits(6) == 2
