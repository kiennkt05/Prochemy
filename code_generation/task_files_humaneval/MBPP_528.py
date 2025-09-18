# MBPP/528
### Completion
def min_length(lists):
    # Check if the input list is empty
    if not lists:
        return (0, [])
    
    # Initialize minimum length to a large number
    min_len = float('inf')
    min_lists = []
    
    # Iterate through each list to find the minimum length
    for lst in lists:
        current_length = len(lst)
        if current_length < min_len:
            min_len = current_length
            min_lists = [lst]  # Start a new list with the current list
        elif current_length == min_len:
            min_lists.append(lst)  # Add to the list of minimum length lists
    
    # Return the minimum length and the first list with that length
    return (min_len, min_lists[0])

# Test case
assert min_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]) == (1, [0])
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert min_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])==(1, [0])
    assert min_length([[1], [5, 7], [10, 12, 14,15]])==(1, [1])
    assert min_length([[5], [15,20,25]])==(1, [5])
