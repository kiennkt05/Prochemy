# MBPP/614
### Completion
def cumulative_sum(tuple_list):
    """
    Calculate the cumulative sum of all values in a list of tuples.

    Parameters:
    tuple_list (list of tuples): A list where each element is a tuple containing numeric values.

    Returns:
    int: The cumulative sum of all numeric values in the tuples.
    """
    total_sum = 0  # Initialize cumulative sum

    # Iterate through each tuple in the list
    for tup in tuple_list:
        # Add each element in the tuple to the total sum
        for value in tup:
            total_sum += value

    return total_sum

# Test case
assert cumulative_sum([(1, 3), (5, 6, 7), (2, 6)]) == 30
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert cummulative_sum([(1, 3), (5, 6, 7), (2, 6)]) == 30
    assert cummulative_sum([(2, 4), (6, 7, 8), (3, 7)]) == 37
    assert cummulative_sum([(3, 5), (7, 8, 9), (4, 8)]) == 44
