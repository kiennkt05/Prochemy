# MBPP/936
### Completion
def re_arrange_tuples(tuples_list, order_list):
    """
    Rearranges the given list of tuples based on the specified order list.

    Parameters:
    tuples_list (list of tuples): The list of tuples to be rearranged.
    order_list (list of int): The list specifying the order of the first elements of the tuples.

    Returns:
    list of tuples: The rearranged list of tuples.
    """
    # Create a dictionary to map the first element of each tuple to the tuple itself
    tuple_dict = {t[0]: t for t in tuples_list}
    
    # Build the result list based on the order_list
    result = [tuple_dict[key] for key in order_list if key in tuple_dict]
    
    return result

# Test case
assert re_arrange_tuples([(4, 3), (1, 9), (2, 10), (3, 2)], [1, 4, 2, 3]) == [(1, 9), (4, 3), (2, 10), (3, 2)]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert re_arrange_tuples([(4, 3), (1, 9), (2, 10), (3, 2)],  [1, 4, 2, 3]) == [(1, 9), (4, 3), (2, 10), (3, 2)]
    assert re_arrange_tuples([(5, 4), (2, 10), (3, 11), (4, 3)],  [3, 4, 2, 3]) == [(3, 11), (4, 3), (2, 10), (3, 11)]
    assert re_arrange_tuples([(6, 3), (3, 8), (5, 7), (2, 4)],  [2, 5, 3, 6]) == [(2, 4), (5, 7), (3, 8), (6, 3)]
