# MBPP/797
### Completion
def sum_in_range(l, r):
    # Initialize the sum
    total_sum = 0
    
    # Iterate through the range from l to r
    for num in range(l, r + 1):
        # Check if the number is odd
        if num % 2 != 0:
            total_sum += num
            
    return total_sum

# Test the function with the provided assertion
assert sum_in_range(2, 5) == 8
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sum_in_Range(2,5) == 8
    assert sum_in_Range(5,7) == 12
    assert sum_in_Range(7,13) == 40
