# MBPP/422
### Completion
def find_Average_Of_Cube(n):
    """
    Calculate the average of the cubes of the first n natural numbers.

    Parameters:
    n (int): The number of natural numbers to consider.

    Returns:
    float: The average of the cubes of the first n natural numbers.
    """
    if n <= 0:
        raise ValueError("n must be a positive integer.")
    
    # Calculate the sum of cubes
    sum_of_cubes = sum(i**3 for i in range(1, n + 1))
    
    # Calculate the average
    average = sum_of_cubes / n
    
    return average

# Test case
assert find_Average_Of_Cube(2) == 4.5
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_Average_Of_Cube(2) == 4.5
    assert find_Average_Of_Cube(3) == 12
    assert find_Average_Of_Cube(1) == 1
