# MBPP/56
### Completion
def check(num):
    # Convert the number to string and reverse it
    reversed_num = int(str(num)[::-1])
    
    # Check if the original number is one less than twice the reversed number
    return num == 2 * reversed_num - 1

# Test the function with the provided assertion
assert check(70) == False
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check(70) == False
    assert check(23) == False
    assert check(73) == True
