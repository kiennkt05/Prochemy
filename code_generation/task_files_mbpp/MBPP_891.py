# MBPP/891
### Completion
def same_length(num1, num2):
    return len(str(abs(num1))) == len(str(abs(num2)))

# Test the function with the provided assertion
assert same_length(12, 1) == False
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert same_Length(12,1) == False
    assert same_Length(2,2) == True
    assert same_Length(10,20) == True
