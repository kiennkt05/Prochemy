# MBPP/346
### Completion
def zigzag(n, k):
    # Base case: if k is 0 or n is 0, the result is 1
    if k == 0 or n == 0:
        return 1
    # Recursive case: calculate the entringer number
    return zigzag(n - 1, k) + zigzag(n, k - 1)

# Test the function with the provided assertion
assert zigzag(4, 3) == 5

# You can add more test cases to verify the function
print("Test passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert zigzag(4, 3) == 5
    assert zigzag(4, 2) == 4
    assert zigzag(3, 1) == 1
