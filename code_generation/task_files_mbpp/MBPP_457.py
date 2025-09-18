# MBPP/457
### Completion
def Find_Min(lists):
    # Check if the input list is empty
    if not lists:
        return []
    
    # Initialize the minimum length and the corresponding sublist
    min_length = float('inf')
    min_sublist = None
    
    # Iterate through each sublist
    for sublist in lists:
        # Update the minimum length and sublist if a shorter one is found
        if len(sublist) < min_length:
            min_length = len(sublist)
            min_sublist = sublist
            
    return min_sublist

# Test the function with the provided assertion
assert Find_Min([[1], [1, 2], [1, 2, 3]]) == [1]
### Test


METADATA = {
    'author': 'mbpp',
    'dataset': 'mbpp'
}

def check(candidate):
    assert Find_Min([[1],[1,2],[1,2,3]]) == [1]
    assert Find_Min([[1,1],[1,1,1],[1,2,7,8]]) == [1,1]
    assert Find_Min([['x'],['x','y'],['x','y','z']]) == ['x']
