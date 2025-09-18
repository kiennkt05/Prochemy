# MBPP/645
### Completion
def find_k_product(tuples_list, k):
    product = 1
    for tup in tuples_list:
        product *= tup[k]
    return product

# Test the function with the provided assertion
assert find_k_product([(5, 6, 7), (1, 3, 5), (8, 9, 19)], 2) == 665
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_k_product([(5, 6, 7), (1, 3, 5), (8, 9, 19)], 2) == 665
    assert find_k_product([(6, 7, 8), (2, 4, 6), (9, 10, 20)], 1) == 280
    assert find_k_product([(7, 8, 9), (3, 5, 7), (10, 11, 21)], 0) == 210
