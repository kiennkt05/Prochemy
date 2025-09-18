# MBPP/645
### Completion
def find_k_product(tuples_list, k):
    """
    Calculate the product of the k-th index elements from a list of tuples.

    Parameters:
    tuples_list (list of tuples): A list containing tuples of integers.
    k (int): The index of the elements to multiply.

    Returns:
    int: The product of the k-th index elements.
    """
    product = 1
    for tup in tuples_list:
        # Check if the tuple has enough elements
        if k < len(tup):
            product *= tup[k]
        else:
            raise IndexError(f"Index {k} is out of range for tuple {tup}")
    
    return product

# Test case
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
