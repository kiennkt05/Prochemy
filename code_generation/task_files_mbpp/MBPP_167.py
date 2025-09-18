# MBPP/167
### Completion
def next_Power_Of_2(n):
    if n <= 0:
        return 1
    power = 1
    while power < n:
        power *= 2
    return power

# Test the function with the provided assertion
assert next_Power_Of_2(0) == 1
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert next_Power_Of_2(0) == 1
    assert next_Power_Of_2(5) == 8
    assert next_Power_Of_2(17) == 32
