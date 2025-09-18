# MBPP/199
### Completion
def highest_Power_of_2(n):
    if n < 1:
        return 0  # Return 0 for numbers less than 1
    power = 1
    while power <= n:
        power *= 2
    return power // 2

# Test the function with the provided assertion
assert highest_Power_of_2(10) == 8
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert highest_Power_of_2(10) == 8
    assert highest_Power_of_2(19) == 16
    assert highest_Power_of_2(32) == 32
