# MBPP/72
### Completion
def dif_Square(n):
    # Check if n is of the form 4k + 2
    return n % 4 != 2

# Test the function with the provided assertion
assert dif_Square(5) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert dif_Square(5) == True
    assert dif_Square(10) == False
    assert dif_Square(15) == True
