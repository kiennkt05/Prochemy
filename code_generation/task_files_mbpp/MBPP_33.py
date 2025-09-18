# MBPP/33
### Completion
def decimal_to_binary(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    return int(bin(n)[2:])  # Convert to binary and remove the '0b' prefix

# Test the function with the provided assertion
assert decimal_to_binary(10) == 1010
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert decimal_To_Binary(10) == 1010
    assert decimal_To_Binary(1) == 1
    assert decimal_To_Binary(20) == 10100
