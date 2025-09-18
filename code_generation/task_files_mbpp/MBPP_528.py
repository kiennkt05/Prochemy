# MBPP/528
### Completion
def min_length(lists):
    # Check if the input list is empty
    if not lists:
        return (0, [])
    
    # Initialize minimum length and the corresponding list
    min_len = float('inf')
    min_list = []

    for lst in lists:
        if len(lst) < min_len:
            min_len = len(lst)
            min_list = lst

    return (min_len, min_list)

# Test the function with the provided assertion
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
