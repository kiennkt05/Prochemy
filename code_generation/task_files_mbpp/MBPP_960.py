# MBPP/960
### Completion
def get_noOfways(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    
    # Initialize the first two values
    prev2 = 1  # This is F(1)
    prev1 = 2  # This is F(2)
    
    # Use dynamic programming to calculate the number of ways
    for i in range(3, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
    
    return prev1

# Test the function with the provided assertion
assert get_noOfways(4) == 3
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert get_noOfways(4)==3
    assert get_noOfways(3)==2
    assert get_noOfways(5)==5
