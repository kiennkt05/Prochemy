# MBPP/646
### Completion
def No_of_cubes(n, k):
    """
    Calculate the number of k-sized cubes in an n-sized cube.
    
    Parameters:
    n (int): The size of the larger cube.
    k (int): The size of the smaller cube.
    
    Returns:
    int: The number of k-sized cubes in the n-sized cube.
    """
    if k > n:
        return 0  # If k is larger than n, no k-sized cubes can fit.
    
    # Calculate the number of k-sized cubes that can fit in each dimension
    count_per_dimension = n - k + 1
    # Total number of k-sized cubes is the cube of count_per_dimension
    return count_per_dimension ** 3

# Test case
assert No_of_cubes(2, 1) == 8  # There are 8 cubes of size 1 in a cube of size 2.
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert No_of_cubes(2,1) == 8
    assert No_of_cubes(5,2) == 64
    assert No_of_cubes(1,1) == 1
