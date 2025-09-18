# MBPP/804
### Completion
def is_Product_Even(numbers, _):
    product = 1
    for number in numbers:
        product *= number
    return product % 2 == 0

# Test the function with the provided assertion
assert is_Product_Even([1, 2, 3], 3) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert is_Product_Even([1,2,3],3) == True
    assert is_Product_Even([1,2,1,4],4) == True
    assert is_Product_Even([1,1],2) == False
