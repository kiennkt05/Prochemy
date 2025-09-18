# MBPP/453
### Completion
def sumofFactors(n):
    even_sum = 0
    for i in range(1, n + 1):
        if n % i == 0 and i % 2 == 0:  # Check if i is a factor and even
            even_sum += i
    return even_sum

# Test the function with the provided assertion
assert sumofFactors(18) == 26
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sumofFactors(18) == 26
    assert sumofFactors(30) == 48
    assert sumofFactors(6) == 8
