# MBPP/724
### Completion
def power_base_sum(base, power):
    # Calculate base raised to the power
    result = base ** power
    
    # Convert the result to a string and sum the digits
    digit_sum = sum(int(digit) for digit in str(result))
    
    return digit_sum

# Test the function with the provided assertion
assert power_base_sum(2, 100) == 115
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert power_base_sum(2,100)==115
    assert power_base_sum(8,10)==37
    assert power_base_sum(8,15)==62
