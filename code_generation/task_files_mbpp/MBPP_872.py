# MBPP/872
### Completion
def check_subset(main_list, subset):
    # Convert the main list to a set of tuples for easier comparison
    main_set = set(tuple(item) for item in main_list)
    # Convert the subset to a set of tuples
    subset_set = set(tuple(item) for item in subset)
    
    # Check if the subset set is a subset of the main set
    return subset_set.issubset(main_set)

# Test the function with the provided assertion
assert check_subset([[1, 3], [5, 7], [9, 11], [13, 15, 17]], [[1, 3], [13, 15, 17]]) == True
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert check_subset([[1, 3], [5, 7], [9, 11], [13, 15, 17]] ,[[1, 3],[13,15,17]])==True
    assert check_subset([[1, 2], [2, 3], [3, 4], [5, 6]],[[3, 4], [5, 6]])==True
    assert check_subset([[[1, 2], [2, 3]], [[3, 4], [5, 7]]],[[[3, 4], [5, 6]]])==False
