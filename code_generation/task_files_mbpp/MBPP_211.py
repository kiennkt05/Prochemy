# MBPP/211
### Completion
def count_Num(n):
    # Count of numbers with 0th and nth bits set
    count = 0
    
    # The range of numbers to check is from 0 to 2^n - 1
    for i in range(1 << n):  # This is equivalent to 2^n
        # Check if the 0th and nth bits are set
        if (i & 1) and (i & (1 << n)):
            count += 1
            
    return count

# Test the function with the provided assertion
assert count_Num(2) == 1
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_Num(2) == 1
    assert count_Num(3) == 2
    assert count_Num(1) == 1
