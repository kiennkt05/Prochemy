# MBPP/707
### Completion
def count_Set_Bits(n):
    # Initialize count of set bits
    count = 0
    
    # Iterate through each bit position
    for i in range(32):  # Assuming 32 bits for the integer representation
        # Calculate the total pairs of 0s and 1s in the current bit position
        total_pairs = (n + 1) // (1 << (i + 1))
        count += total_pairs * (1 << i)
        
        # Calculate the remaining bits after the last complete pair
        remainder = (n + 1) % (1 << (i + 1))
        count += max(0, remainder - (1 << i))
    
    return count

# Test the function with the provided test case
assert count_Set_Bits(16) == 33

# Additional test cases can be added to verify correctness
print(count_Set_Bits(16))  # Output: 33
print(count_Set_Bits(5))   # Output: 7
print(count_Set_Bits(7))   # Output: 12
print(count_Set_Bits(8))   # Output: 16
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_Set_Bits(16) == 33
    assert count_Set_Bits(2) == 2
    assert count_Set_Bits(14) == 28
