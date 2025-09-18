# MBPP/167
### Completion
def next_Power_Of_2(n):
    # Handle the special case for n = 0
    if n <= 0:
        return 1
    
    power = 1  # Start with the smallest power of 2 (2^0)
    
    # Keep doubling the power until it is greater than or equal to n
    while power < n:
        power *= 2
    
    return power

# Test cases
assert next_Power_Of_2(0) == 1
assert next_Power_Of_2(1) == 1
assert next_Power_Of_2(2) == 2
assert next_Power_Of_2(3) == 4
assert next_Power_Of_2(4) == 4
assert next_Power_Of_2(5) == 8
assert next_Power_Of_2(15) == 16
assert next_Power_Of_2(16) == 16
assert next_Power_Of_2(17) == 32

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert next_Power_Of_2(0) == 1
    assert next_Power_Of_2(5) == 8
    assert next_Power_Of_2(17) == 32
