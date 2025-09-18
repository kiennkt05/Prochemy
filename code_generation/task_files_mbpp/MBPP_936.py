# MBPP/936
### Completion
def re_arrange_tuples(tuples_list, order):
    # Create a dictionary to map the first element of each tuple to the tuple itself
    tuple_dict = {t[0]: t for t in tuples_list}
    
    # Use the order list to create a new list of tuples in the specified order
    arranged_tuples = [tuple_dict[i] for i in order if i in tuple_dict]
    
    return arranged_tuples

# Example usage
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
