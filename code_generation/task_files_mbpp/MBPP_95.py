# MBPP/95
### Completion
def Find_Min_Length(lst):
    # Check if the input list is empty
    if not lst:
        return 0  # Return 0 if there are no sublists
    
    # Use a generator expression to find the minimum length of sublists
    min_length = min(len(sublist) for sublist in lst)
    
    return min_length

# Test the function with the provided assertion
assert Find_Min_Length([[1], [1, 2]]) == 1
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert Find_Min_Length([[1],[1,2]]) == 1
    assert Find_Min_Length([[1,2],[1,2,3],[1,2,3,4]]) == 2
    assert Find_Min_Length([[3,3,3],[4,4,4,4]]) == 3
