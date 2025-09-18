# MBPP/957
### Completion
def get_First_Set_Bit_Pos(n):
    if n == 0:
        return -1  # Return -1 if there are no set bits
    position = 1
    while (n & 1) == 0:
        n >>= 1
        position += 1
    return position

# Test the function with the provided assertion
assert get_First_Set_Bit_Pos(12) == 3
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert get_First_Set_Bit_Pos(12) == 3
    assert get_First_Set_Bit_Pos(18) == 2
    assert get_First_Set_Bit_Pos(16) == 5
