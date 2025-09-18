# MBPP/446
### Completion
def count_Occurrence(tup, lst):
    """
    Count the occurrences of all elements in the list within the tuple.

    Parameters:
    tup (tuple): A tuple containing elements to be counted.
    lst (list): A list of elements whose occurrences in the tuple are to be counted.

    Returns:
    int: The total count of occurrences of the list elements in the tuple.
    """
    total_count = 0  # Initialize the counter

    # Iterate through each element in the list
    for element in lst:
        # Count occurrences of the element in the tuple and add to total_count
        total_count += tup.count(element)

    return total_count

# Test case
assert count_Occurrence(('a', 'a', 'c', 'b', 'd'), ['a', 'b']) == 3
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b'] ) == 3
    assert count_Occurrence((1, 2, 3, 1, 4, 6, 7, 1, 4),[1, 4, 7]) == 6
    assert count_Occurrence((1,2,3,4,5,6),[1,2]) == 2
