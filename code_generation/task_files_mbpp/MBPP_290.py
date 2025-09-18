# MBPP/290
### Completion
def max_length(lists):
    # Initialize variables to track the maximum length and the corresponding list
    max_len = 0
    max_list = []
    
    # Iterate through each list in the input
    for lst in lists:
        # Check if the current list is longer than the maximum found so far
        if len(lst) > max_len:
            max_len = len(lst)
            max_list = lst
            
    return (max_len, max_list)

# Test the function with the provided assertion
assert max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]) == (3, [13, 15, 17])
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])==(3, [13, 15, 17])
    assert max_length([[1], [5, 7], [10, 12, 14,15]])==(4, [10, 12, 14,15])
    assert max_length([[5], [15,20,25]])==(3, [15,20,25])
