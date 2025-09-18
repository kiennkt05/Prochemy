# MBPP/120
### Completion
def max_product_tuple(tuples_list):
    max_product = float('-inf')  # Initialize to negative infinity
    for a, b in tuples_list:
        product = a * b
        if product > max_product:
            max_product = product
    return max_product

# Test the function with the provided assertion
assert max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)]) == 36
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)] )==36
    assert max_product_tuple([(10,20), (15,2), (5,10)] )==200
    assert max_product_tuple([(11,44), (10,15), (20,5), (12, 9)] )==484
