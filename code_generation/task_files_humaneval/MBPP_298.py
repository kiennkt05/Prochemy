# MBPP/298
### Completion
def intersection_nested_lists(main_list, nested_list):
    """
    Find the elements in each sublist of a nested list that are present in the main list.

    Parameters:
    main_list (list): A list of elements to check against.
    nested_list (list of list): A nested list containing sublists of elements.

    Returns:
    list of list: A new nested list containing only the elements that are present in the main list.
    """
    result = []
    
    for sublist in nested_list:
        # Find intersection of the main list and the current sublist
        intersection = [item for item in sublist if item in main_list]
        result.append(intersection)
    
    return result

# Test case
assert intersection_nested_lists(
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
    [[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]]
) == [[12], [7, 11], [1, 5, 8]]

print("Test case passed!")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert intersection_nested_lists( [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],[[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]])==[[12], [7, 11], [1, 5, 8]]
    assert intersection_nested_lists([[2, 3, 1], [4, 5], [6, 8]], [[4, 5], [6, 8]])==[[], []]
    assert intersection_nested_lists(['john','amal','joel','george'],[['john'],['jack','john','mary'],['howard','john'],['jude']])==[['john'], ['john'], ['john'], []]
