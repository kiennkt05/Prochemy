# MBPP/392
### Completion
def get_max_sum(n):
    # Base case: if n is 0, the maximum sum is 0
    if n == 0:
        return 0
    
    # Recursive case: calculate the maximum sum using the given equation
    max_sum = max(get_max_sum(n // 2) + get_max_sum(n // 3) + get_max_sum(n // 4) + get_max_sum(n // 5), n)
    
    return max_sum

# Test the function with the provided assertion
assert get_max_sum(60) == 106

# You can also add more test cases to verify the function
print(get_max_sum(60))  # Output: 106
print(get_max_sum(10))   # Example output
print(get_max_sum(100))  # Example output
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert get_max_sum(60) == 106
    assert get_max_sum(10) == 12
    assert get_max_sum(2) == 2
