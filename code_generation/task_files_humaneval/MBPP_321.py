# MBPP/321
### Completion
def find_demlo(number: str) -> str:
    # Determine the length of the input number
    n = len(number)
    
    # Create the ascending part of the demlo number
    ascending_part = ''.join(str(i) for i in range(1, n + 1))
    
    # Create the descending part of the demlo number
    descending_part = ''.join(str(i) for i in range(n - 1, 0, -1))
    
    # Combine both parts to form the demlo number
    demlo_number = ascending_part + descending_part
    
    return demlo_number

# Test the function with the provided assertion
assert find_demlo("111111") == '12345654321'

# Additional test cases
assert find_demlo("1") == '1'
assert find_demlo("22") == '121'
assert find_demlo("333") == '12321'
assert find_demlo("4444") == '1234321'
assert find_demlo("55555") == '1234554321'

print("All tests passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_demlo("111111") == '12345654321'
    assert find_demlo("1111") == '1234321'
    assert find_demlo("13333122222") == '123456789101110987654321'
