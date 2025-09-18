# MBPP/671
### Completion
def set_Right_most_Unset_Bit(n):
    # Find the rightmost unset bit and set it
    return n | (n + 1) & ~(n)

# Test the function with the provided assertion
assert set_Right_most_Unset_Bit(21) == 23
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert set_Right_most_Unset_Bit(21) == 23
    assert set_Right_most_Unset_Bit(11) == 15
    assert set_Right_most_Unset_Bit(15) == 15
