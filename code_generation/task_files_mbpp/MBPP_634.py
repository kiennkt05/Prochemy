# MBPP/634
### Completion
def even_Power_Sum(n):
    # Calculate the sum of the fourth power of the first n even natural numbers
    return sum((2 * i) ** 4 for i in range(1, n + 1))

# Test the function with the provided assertion
assert even_Power_Sum(2) == 272
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert even_Power_Sum(2) == 272
    assert even_Power_Sum(3) == 1568
    assert even_Power_Sum(4) == 5664
