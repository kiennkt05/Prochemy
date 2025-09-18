# MBPP/334
### Completion
def check_Validity(a, b, c):
    # Check the triangle inequality conditions
    return (a + b > c) and (a + c > b) and (b + c > a)

# Example assertion to test the function
assert check_Validity(1, 2, 3) == False
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_Validity(1,2,3) == False
    assert check_Validity(2,3,5) == False
    assert check_Validity(7,10,5) == True
