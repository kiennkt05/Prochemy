# MBPP/75
### Completion
def find_tuples(tuples_list, k):
    """
    Find tuples in the given list where all elements are divisible by k.

    Parameters:
    tuples_list (list of tuples): A list of tuples to check.
    k (int): The divisor to check for divisibility.

    Returns:
    str: A string representation of the list of tuples that meet the criteria.
    """
    # Initialize an empty list to store the result
    result = []
    
    # Iterate through each tuple in the provided list
    for tup in tuples_list:
        # Check if all elements in the tuple are divisible by k
        if all(element % k == 0 for element in tup):
            result.append(tup)
    
    # Return the result as a string representation
    return str(result)

# Test the function with the provided test case
assert find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6) == '[(6, 24, 12)]'
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6) == '[(6, 24, 12)]'
    assert find_tuples([(5, 25, 30), (4, 2, 3), (7, 8, 9)], 5) == '[(5, 25, 30)]'
    assert find_tuples([(7, 9, 16), (8, 16, 4), (19, 17, 18)], 4) == '[(8, 16, 4)]'
