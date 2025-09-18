# MBPP/194
### Completion
def octal_To_Decimal(octal):
    decimal = 0
    octal_str = str(octal)
    length = len(octal_str)
    
    for i in range(length):
        digit = int(octal_str[length - 1 - i])
        decimal += digit * (8 ** i)
    
    return decimal

# Test the function with the provided assertion
assert octal_To_Decimal(25) == 21
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert octal_To_Decimal(25) == 21
    assert octal_To_Decimal(30) == 24
    assert octal_To_Decimal(40) == 32
