# MBPP/573
### Completion
def unique_product(numbers):
    unique_numbers = set(numbers)  # Get unique numbers using a set
    product = 1
    for number in unique_numbers:
        product *= number  # Multiply each unique number
    return product

# Test the function with the provided assertion
assert unique_product([10, 20, 30, 40, 20, 50, 60, 40]) == 720000000
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert unique_product([10, 20, 30, 40, 20, 50, 60, 40]) ==  720000000
    assert unique_product([1, 2, 3, 1,]) == 6
    assert unique_product([7, 8, 9, 0, 1, 1]) == 0
