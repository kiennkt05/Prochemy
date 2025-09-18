# MBPP/855
### Completion
def check_Even_Parity(number):
    # Count the number of 1s in the binary representation of the number
    count_of_ones = bin(number).count('1')
    # Check if the count of 1s is even
    return count_of_ones % 2 == 0

# Test the function with the provided assertion
assert check_Even_Parity(10) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_Even_Parity(10) == True
    assert check_Even_Parity(11) == False
    assert check_Even_Parity(18) == True
