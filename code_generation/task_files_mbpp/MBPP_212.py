# MBPP/212
### Completion
def fourth_Power_Sum(n):
    return sum(i**4 for i in range(1, n + 1))

# Test the function with the provided assertion
assert fourth_Power_Sum(2) == 17
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert fourth_Power_Sum(2) == 17
    assert fourth_Power_Sum(4) == 354
    assert fourth_Power_Sum(6) == 2275
