# MBPP/698
### Completion
def sort_dict_item(input_dict):
    """
    Sorts the dictionary items by the product of the tuple keys.

    Parameters:
    input_dict (dict): A dictionary with tuple keys.

    Returns:
    dict: A new dictionary sorted by the product of the keys.
    """
    # Create a sorted list of items based on the product of the tuple keys
    sorted_items = sorted(input_dict.items(), key=lambda item: item[0][0] * item[0][1])
    
    # Convert the sorted list of items back into a dictionary
    sorted_dict = dict(sorted_items)
    
    return sorted_dict

# Test case
assert sort_dict_item({(5, 6): 3, (2, 3): 9, (8, 4): 10, (6, 4): 12}) == {(2, 3): 9, (6, 4): 12, (5, 6): 3, (8, 4): 10}
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert sort_dict_item({(5, 6) : 3, (2, 3) : 9, (8, 4): 10, (6, 4): 12} ) == {(2, 3): 9, (6, 4): 12, (5, 6): 3, (8, 4): 10}
    assert sort_dict_item({(6, 7) : 4, (3, 4) : 10, (9, 5): 11, (7, 5): 13} ) == {(3, 4): 10, (7, 5): 13, (6, 7): 4, (9, 5): 11}
    assert sort_dict_item({(7, 8) : 5, (4, 5) : 11, (10, 6): 12, (8, 6): 14} ) == {(4, 5): 11, (8, 6): 14, (7, 8): 5, (10, 6): 12}
