# MBPP/712
### Completion
def remove_duplicate(lst):
    """
    Remove duplicates from a list of lists.

    Parameters:
    lst (list of list): A list containing sublists.

    Returns:
    list of list: A new list with duplicates removed.
    """
    seen = set()  # To track seen sublists
    result = []   # To store the result without duplicates

    for sublist in lst:
        # Convert the sublist to a tuple to make it hashable
        tuple_sublist = tuple(sublist)
        if tuple_sublist not in seen:
            seen.add(tuple_sublist)  # Mark this sublist as seen
            result.append(sublist)    # Add the original sublist to the result

    return result

# Test case
assert remove_duplicate([[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]) == [[10, 20], [40], [30, 56, 25], [33]]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert remove_duplicate([[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]])==[[10, 20], [30, 56, 25], [33], [40]] 
    assert remove_duplicate(["a", "b", "a", "c", "c"] )==["a", "b", "c"]
    assert remove_duplicate([1, 3, 5, 6, 3, 5, 6, 1] )==[1, 3, 5, 6]
