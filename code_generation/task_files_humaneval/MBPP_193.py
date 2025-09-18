# MBPP/193
### Completion
def remove_tuple(input_tuple):
    """
    Remove duplicates from the given tuple while maintaining the order of elements.

    Parameters:
    input_tuple (tuple): The tuple from which duplicates need to be removed.

    Returns:
    tuple: A new tuple containing only the unique elements from the input tuple.
    """
    seen = set()  # To track seen elements
    unique_list = []  # To store unique elements in order

    for item in input_tuple:
        if item not in seen:
            seen.add(item)  # Mark this item as seen
            unique_list.append(item)  # Add to unique list

    return tuple(unique_list)  # Convert the list back to a tuple

# Test case
assert remove_tuple((1, 3, 5, 2, 3, 5, 1, 1, 3)) == (1, 2, 3, 5)
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert remove_tuple((1, 3, 5, 2, 3, 5, 1, 1, 3)) == (1, 2, 3, 5)
    assert remove_tuple((2, 3, 4, 4, 5, 6, 6, 7, 8, 8)) == (2, 3, 4, 5, 6, 7, 8)
    assert remove_tuple((11, 12, 13, 11, 11, 12, 14, 13)) == (11, 12, 13, 14)
