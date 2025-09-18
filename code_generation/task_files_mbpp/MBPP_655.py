# MBPP/655
### Completion
def fifth_Power_Sum(n):
    return sum(i**5 for i in range(1, n + 1))

# Test the function with the provided assertion
assert fifth_Power_Sum(2) == 33
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert fifth_Power_Sum(2) == 33
    assert fifth_Power_Sum(4) == 1300
    assert fifth_Power_Sum(3) == 276
