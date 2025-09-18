# MBPP/56
### Completion
def check(n):
    # Convert the number to string to reverse it
    reversed_n = int(str(n)[::-1])
    
    # Calculate twice the reversed number
    twice_reversed = 2 * reversed_n
    
    # Check if the original number is one less than twice the reversed number
    return n == (twice_reversed - 1)

# Test case
assert check(70) == False  # As per the provided test case
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check(70) == False
    assert check(23) == False
    assert check(73) == True
