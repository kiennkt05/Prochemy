# MBPP/948
### Completion
def get_item(tup, index):
    """
    Retrieve an item from a tuple at a specified index and return it as a single-element tuple.

    Parameters:
    tup (tuple): The tuple from which to retrieve the item.
    index (int): The index of the item to retrieve.

    Returns:
    tuple: A single-element tuple containing the item at the specified index.
    """
    # Access the item at the specified index and return it as a single-element tuple
    return (tup[index],)

# Test case
assert get_item(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"), 3) == ('e',)

# If the assertion passes, the function works as expected.
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert get_item(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),3)==('e')
    assert get_item(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),-4)==('u')
    assert get_item(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),-3)==('r')
