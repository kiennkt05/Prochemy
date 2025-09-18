# MBPP/321
### Completion
def find_demlo(num_str):
    # Convert the input string to a list of digits
    digits = [int(d) for d in num_str]
    
    # Create the ascending part of the demlo number
    ascending_part = ''.join(str(i) for i in range(1, max(digits) + 1))
    
    # Create the descending part of the demlo number
    descending_part = ascending_part[-2::-1]  # Skip the last digit to avoid duplication
    
    # Combine both parts to form the demlo number
    demlo_number = ascending_part + descending_part
    
    return demlo_number

# Test the function with the provided assertion
assert find_demlo("111111") == '12345654321'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_demlo("111111") == '12345654321'
    assert find_demlo("1111") == '1234321'
    assert find_demlo("13333122222") == '123456789101110987654321'
