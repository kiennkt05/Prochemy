# MBPP/370
### Completion
def float_sort(items):
    """
    Sorts a list of tuples based on the float value of the second element in each tuple.

    Args:
    items (list of tuples): A list where each tuple contains an item name and a string representation of a float.

    Returns:
    list of tuples: The sorted list of tuples in descending order based on the float value.
    """
    # Sort the list of tuples by converting the second element to float
    sorted_items = sorted(items, key=lambda x: float(x[1]), reverse=True)
    return sorted_items

# Test case
assert float_sort([('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]) == [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert float_sort([('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')])==[('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')] 
    assert float_sort([('item1', '15'), ('item2', '10'), ('item3', '20')])==[('item3', '20'), ('item1', '15'), ('item2', '10')] 
    assert float_sort([('item1', '5'), ('item2', '10'), ('item3', '14')])==[('item3', '14'), ('item2', '10'), ('item1', '5')] 
