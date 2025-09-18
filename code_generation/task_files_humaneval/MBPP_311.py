# MBPP/311
### Completion
def set_left_most_unset_bit(n):
    # Find the position of the leftmost unset bit
    position = 0
    temp = n
    
    # Shift right until we find the first unset bit
    while temp > 0:
        if temp & 1 == 0:  # Check if the current bit is unset
            break
        position += 1
        temp >>= 1
    
    # If we finished the loop and temp is 0, it means all bits are set
    # We need to set the next bit (which is position)
    if temp == 0:
        return n | (1 << position)
    
    # Set the leftmost unset bit
    return n | (1 << position)

# Test the function with the provided test case
assert set_left_most_unset_bit(10) == 14  # 10 in binary is 1010, setting the leftmost unset bit gives 1110 (14)
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert set_left_most_unset_bit(10) == 14
    assert set_left_most_unset_bit(12) == 14
    assert set_left_most_unset_bit(15) == 15
