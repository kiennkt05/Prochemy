# MBPP/216
### Completion
def check_subset_list(main_list, nested_list):
    # Flatten the nested list to make it easier to check for subsets
    flat_nested_list = [item for sublist in nested_list for item in sublist]
    
    # Check if all elements in the flattened nested list are in the main list
    return all(item in main_list for item in flat_nested_list)

# Test the function with the provided assertion
assert check_subset_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], [[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]]) == False
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_subset_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],[[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]])==False
    assert check_subset_list([[2, 3, 1], [4, 5], [6, 8]],[[4, 5], [6, 8]])==True
    assert check_subset_list([['a', 'b'], ['e'], ['c', 'd']],[['g']])==False
