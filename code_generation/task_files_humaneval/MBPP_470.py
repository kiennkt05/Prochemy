# MBPP/470
### Completion
def add_pairwise(tup):
    """
    This function takes a tuple of numbers and returns a tuple containing the pairwise sums.
    
    Parameters:
    tup (tuple): A tuple of numbers.
    
    Returns:
    tuple: A tuple containing the pairwise sums.
    """
    # Calculate pairwise sums using a list comprehension
    pairwise_sums = (tup[i] + tup[i + 1] for i in range(len(tup) - 1))
    
    # Convert the generator to a tuple and return
    return tuple(pairwise_sums)

# Test the function with the provided test case
assert add_pairwise((1, 5, 7, 8, 10)) == (6, 12, 15, 18)

# You can add more test cases if needed
print("Test passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert add_pairwise((1, 5, 7, 8, 10)) == (6, 12, 15, 18)
    assert add_pairwise((2, 6, 8, 9, 11)) == (8, 14, 17, 20)
    assert add_pairwise((3, 7, 9, 10, 12)) == (10, 16, 19, 22)
