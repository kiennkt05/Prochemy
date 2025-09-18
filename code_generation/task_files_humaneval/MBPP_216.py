# MBPP/216
### Completion
def flatten(nested_list):
    """Flatten a nested list into a single list."""
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten(item))  # Recursively flatten if item is a list
        else:
            flat_list.append(item)  # Append the item if it's not a list
    return flat_list

def check_subset_list(main_list, subset_list):
    """
    Check if subset_list is a subset of main_list.
    
    Parameters:
    main_list (list): The main list to check against.
    subset_list (list): The nested list to check if it's a subset.
    
    Returns:
    bool: True if subset_list is a subset of main_list, False otherwise.
    """
    # Flatten both lists
    flat_main_list = flatten(main_list)
    flat_subset_list = flatten(subset_list)
    
    # Check if all elements in flat_subset_list are in flat_main_list
    return all(item in flat_main_list for item in flat_subset_list)

# Test case
assert check_subset_list(
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
    [[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]]
) == False

print("Test case passed.")
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_subset_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],[[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]])==False
    assert check_subset_list([[2, 3, 1], [4, 5], [6, 8]],[[4, 5], [6, 8]])==True
    assert check_subset_list([['a', 'b'], ['e'], ['c', 'd']],[['g']])==False
