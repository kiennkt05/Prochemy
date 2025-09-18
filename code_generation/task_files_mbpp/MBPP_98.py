# MBPP/98
### Completion
def multiply_num(numbers):
    # Calculate the product of all numbers
    product = 1
    for num in numbers:
        product *= num
    
    # Divide the product by the length of the list
    result = product / len(numbers)
    return result

# Test the function with the provided assertion
assert multiply_num((8, 2, 3, -1, 7)) == -67.2
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert multiply_num((8, 2, 3, -1, 7))==-67.2
    assert multiply_num((-10,-20,-30))==-2000.0
    assert multiply_num((19,15,18))==1710.0
