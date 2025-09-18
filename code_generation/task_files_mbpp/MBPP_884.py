# MBPP/884
### Completion
def all_Bits_Set_In_The_Given_Range(num, start, end):
    # Create a mask for the bits in the given range
    mask = ((1 << (end - start + 1)) - 1) << start
    
    # Check if the bits in the range are set in the number
    return (num & mask) == mask

# Test the function with the provided assertion
assert all_Bits_Set_In_The_Given_Range(10, 2, 1) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert all_Bits_Set_In_The_Given_Range(10,2,1) == True 
    assert all_Bits_Set_In_The_Given_Range(5,2,4) == False
    assert all_Bits_Set_In_The_Given_Range(22,2,3) == True 
