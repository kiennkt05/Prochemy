# MBPP/710
### Completion
def front_and_rear(record):
    """
    This function takes a tuple and returns a new tuple containing
    the first and last elements of the input tuple.

    Parameters:
    record (tuple): A tuple from which to extract the first and last elements.

    Returns:
    tuple: A tuple containing the first and last elements of the input tuple.
    """
    # Access the first element
    first_element = record[0]
    # Access the last element
    last_element = record[-1]
    # Return a tuple with the first and last elements
    return (first_element, last_element)

# Test case
assert front_and_rear((10, 4, 5, 6, 7)) == (10, 7)

# Additional test cases for verification
assert front_and_rear((1, 2, 3)) == (1, 3)
assert front_and_rear(('a', 'b', 'c')) == ('a', 'c')
assert front_and_rear((True, False, True)) == (True, True)
assert front_and_rear((100,)) == (100, 100)  # Single element case

print("All test cases passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert front_and_rear((10, 4, 5, 6, 7)) == (10, 7)
    assert front_and_rear((1, 2, 3, 4, 5)) == (1, 5)
    assert front_and_rear((6, 7, 8, 9, 10)) == (6, 10)
