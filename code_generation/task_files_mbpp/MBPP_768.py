# MBPP/768
### Completion
def check_Odd_Parity(num):
    # Count the number of 1s in the binary representation of the number
    count_of_ones = bin(num).count('1')
    # Check if the count of 1s is odd
    return count_of_ones % 2 == 1

# Test the function with the provided assertion
assert check_Odd_Parity(13) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_Odd_Parity(13) == True
    assert check_Odd_Parity(21) == True
    assert check_Odd_Parity(18) == False
