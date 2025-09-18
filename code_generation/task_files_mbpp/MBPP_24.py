# MBPP/24
### Completion
def binary_to_decimal(binary):
    decimal = 0
    binary_str = str(binary)[::-1]  # Reverse the string for easier calculation
    for index, digit in enumerate(binary_str):
        decimal += int(digit) * (2 ** index)
    return decimal

# Test the function with the provided assertion
assert binary_to_decimal(100) == 4
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert binary_to_decimal(100) == 4
    assert binary_to_decimal(1011) == 11
    assert binary_to_decimal(1101101) == 109
