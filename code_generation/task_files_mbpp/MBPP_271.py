# MBPP/271
### Completion
def even_Power_Sum(n):
    # Calculate the sum of the fifth power of the first n even natural numbers
    return sum((2 * i) ** 5 for i in range(1, n + 1))

# Test the function with the provided assertion
assert even_Power_Sum(2) == 1056
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert even_Power_Sum(2) == 1056
    assert even_Power_Sum(3) == 8832
    assert even_Power_Sum(1) == 32
