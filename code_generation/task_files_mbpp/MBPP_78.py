# MBPP/78
### Completion
def count_set_bits(num):
    """Helper function to count the number of set bits in an integer."""
    count = 0
    while num:
        count += num & 1
        num >>= 1
    return count

def count_With_Odd_SetBits(n):
    """Function to count the number of integers with an odd number of set bits from 1 to n."""
    odd_count = 0
    for i in range(1, n + 1):
        if count_set_bits(i) % 2 == 1:  # Check if the count of set bits is odd
            odd_count += 1
    return odd_count

# Test the function with the provided assertion
assert count_With_Odd_SetBits(5) == 3
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_With_Odd_SetBits(5) == 3
    assert count_With_Odd_SetBits(10) == 5
    assert count_With_Odd_SetBits(15) == 8
