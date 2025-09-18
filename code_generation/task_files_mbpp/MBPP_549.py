# MBPP/549
### Completion
def odd_Num_Sum(n):
    # Calculate the sum of the fifth power of the first n odd natural numbers
    return sum((2 * i + 1) ** 5 for i in range(n))

# Test the function with the provided assertion
assert odd_Num_Sum(1) == 1
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert odd_Num_Sum(1) == 1
    assert odd_Num_Sum(2) == 244
    assert odd_Num_Sum(3) == 3369
