# MBPP/228
### Completion
def all_Bits_Set_In_The_Given_Range(num, start, end):
    # Create a mask with bits set to 1 in the specified range
    mask = ((1 << (end - start + 1)) - 1) << start
    
    # Check if the bits in the range are unset
    return (num & mask) == 0

# Test the function with the provided assertion
assert all_Bits_Set_In_The_Given_Range(4, 1, 2) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert all_Bits_Set_In_The_Given_Range(4,1,2) == True
    assert all_Bits_Set_In_The_Given_Range(17,2,4) == True
    assert all_Bits_Set_In_The_Given_Range(39,4,6) == False
