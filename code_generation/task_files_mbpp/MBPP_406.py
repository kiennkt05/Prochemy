# MBPP/406
### Completion
def find_Parity(number):
    if number % 2 == 0:
        return "Even Parity"
    else:
        return "Odd Parity"

# Test the function with the provided assertion
assert find_Parity(12) == "Even Parity"
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_Parity(12) == "Even Parity"
    assert find_Parity(7) == "Odd Parity"
    assert find_Parity(10) == "Even Parity"
